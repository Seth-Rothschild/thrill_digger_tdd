import pytest
import hypothesis

import thrill_digger_tdd

def test_thrill_digger_tdd_version():
    """Test that the package exists and has a version"""
    assert thrill_digger_tdd.__version__

