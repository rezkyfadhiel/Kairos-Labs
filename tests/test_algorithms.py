"""
Unit tests for quantum algorithms.
"""

import pytest
from src.quantum.algorithms import ShorsAlgorithm, Grover

class TestShorsAlgorithm:
    
    def test_factor_15(self):
        """Test factoring 15 = 3 × 5"""
        shor = ShorsAlgorithm(15)
        factors = shor.factor()
        assert factors is not None
        assert factors[0] * factors[1] == 15
    
    def test_factor_21(self):
        """Test factoring 21 = 3 × 7"""
        shor = ShorsAlgorithm(21)
        factors = shor.factor()
        assert factors is not None
        assert factors[0] * factors[1] == 21
      
