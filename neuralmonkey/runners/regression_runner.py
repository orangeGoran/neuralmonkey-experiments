from typing import Dict, List, Set, Callable

import numpy as np
import tensorflow as tf
from typeguard import check_argument_types

from neuralmonkey.decoders.sequence_regressor import SequenceRegressor
from neuralmonkey.model.model_part import ModelPart
from neuralmonkey.runners.base_runner import (
    BaseRunner, Executable, ExecutionResult, NextExecute)

# pylint: disable=invalid-name
Postprocessor = Callable[[List[float]], List[float]]
# pylint: enable=invalid-name


class RegressionRunExecutable(Executable):

    def __init__(self,
                 all_coders: Set[ModelPart],
                 fetches: Dict[str, tf.Tensor],
                 postprocess: Postprocessor) -> None:
        self._all_coders = all_coders
        self._fetches = fetches
        self._postprocess = postprocess

        self.result = None  # type: ExecutionResult

    def next_to_execute(self) -> NextExecute:
        """Get the feedables and tensors to run."""
        return self._all_coders, self._fetches, None

    def collect_results(self, results: List[Dict]) -> None:
        predictions_sum = np.zeros_like(results[0]["prediction"])
        mse_loss = 0.

        for sess_result in results:
            if "mse" in sess_result:
                mse_loss += sess_result["mse"]

            predictions_sum += sess_result["prediction"]

        predictions = predictions_sum / len(results)

        if self._postprocess is not None:
            predictions = self._postprocess(predictions)

        self.result = ExecutionResult(
            outputs=predictions.tolist(),
            losses=[mse_loss],
            scalar_summaries=None,
            histogram_summaries=None,
            image_summaries=None)


class RegressionRunner(BaseRunner[SequenceRegressor]):
    """A runnner that takes the predictions of a sequence regressor."""

    def __init__(self,
                 output_series: str,
                 decoder: SequenceRegressor,
                 postprocess: Postprocessor = None) -> None:
        check_argument_types()
        BaseRunner[SequenceRegressor].__init__(self, output_series, decoder)

        self._postprocess = postprocess

    # pylint: disable=unused-argument
    def get_executable(self,
                       compute_losses: bool,
                       summaries: bool,
                       num_sessions: int) -> Executable:
        fetches = {"prediction": self._decoder.predictions}
        if compute_losses:
            fetches["mse"] = self._decoder.cost

        return RegressionRunExecutable(
            self.all_coders, fetches, self._postprocess)
    # pylint: enable=unused-argument

    @property
    def loss_names(self) -> List[str]:
        return ["mse"]
