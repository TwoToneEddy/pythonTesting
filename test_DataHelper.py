from dataHelper import DataHelper
import pytest

helperBasic = DataHelper("tests/eventsFittedBasicTest.csv")
helperMissingData = DataHelper("tests/eventsFittedMissingDataTest.csv")
helperMissingField = DataHelper("tests/eventsFittedMissingFieldTest.csv")


def test_calc_average_mass():
    """Test correct mean is calculated on known dataset"""
    assert helperBasic.calc_average_mass() == 165.5


def test_calc_median_mass():
    """Test correct median is calculated on known dataset"""
    assert helperBasic.calc_median_mass() == 165.5


def test_calc_average_mass_exception_missing_data():
    """Test correct exception is thrown when calc_average_mass() called on incomplete
    dataset"""
    with pytest.raises(ValueError) as e:
        a = helperMissingData.calc_average_mass()


def test_calc_average_median_exception_missing_data():
    """Test correct exception is thrown when calc_median_mass() called on incomplete
    dataset"""
    with pytest.raises(ValueError) as e:
        a = helperMissingData.calc_median_mass()


def test_calc_average_mass_exception_missing_field():
    """Test correct exception is thrown when calc_average_mass() called on data
    where the masses_kDa field is missing"""
    with pytest.raises(ValueError) as e:
        a = helperMissingField.calc_average_mass()


def test_calc_average_median_exception_missing_field():
    """Test correct exception is thrown when calc_median_mass() called on data
    where the masses_kDa field is missing"""
    with pytest.raises(ValueError) as e:
        a = helperMissingField.calc_median_mass()