
import numpy as np
import pytest

from detector import predict_observations, load_model


@pytest.fixture
def model():
    return load_model()


def test_predictions_have_correct_shape(model):
    X=np.array([[0.2,-0.3],[7.0,7.0]])

    predictions=predict_observations(model,X)

    assert predictions.shape == (2,)


def test_predictions_use_valid_labels(model):
    X=np.array([[0.2,-0.3],[7.0,7.0]])

    predictions=predict_observations(model,X)

    assert set(predictions).issubset({0,1})


def test_invalid_feature_count_is_rejected(model):
    X=np.array([[1.0,2.0,3.0]])

    with pytest.raises(ValueError):
        predict_observations(model,X)


def test_non_finite_values_are_rejected(model):
    X = np.array([[np.nan, 1.0]])

    with pytest.raises(ValueError):
        predict_observations(model, X)


def test_empty_input_is_rejected(model):
    X = np.empty((0, 2))

    with pytest.raises(ValueError):
        predict_observations(model, X)
