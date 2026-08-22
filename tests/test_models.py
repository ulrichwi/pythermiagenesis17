from pythermiagenesis import ThermiaGenesis
from pythermiagenesis.const import *

def test_legacy_model_identifiers_unchanged():
    assert MODEL_MEGA == "mega"
    assert MODEL_INVERTER == "inverter"

def test_new_models_and_aliases():
    assert MODEL_ALIASES["thermia calibra rxt"] == MODEL_CALIBRA_RXT
    assert MODEL_ALIASES["stiebel-eltron wpe-i 07.1"] == MODEL_STIEBEL_WPE_I_071
    assert REGISTER_RANGES[MODEL_CALIBRA_RXT] == REGISTER_RANGES[MODEL_STIEBEL_WPE_I_071]

def test_v17_register_flags():
    assert REGISTERS[ATTR_INPUT_CONTROL_SOFTWARE_VERSION_MAJOR][MODEL_CALIBRA_RXT]
    assert REGISTERS[ATTR_INPUT_OUTDOOR_TEMPERATURE][MODEL_CALIBRA_RXT]
    assert not REGISTERS[ATTR_INPUT_CONTROL_SOFTWARE_VERSION_MAJOR][MODEL_INVERTER]
