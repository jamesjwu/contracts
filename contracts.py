"""
Simple tools for writing pre and post conditions in python
"""
import inspect
#To use contracts, set DEBUG.contracts to be True
class DEBUG(object):
	contracts = True

def requires(stmt):
	if DEBUG.contracts:
		if not stmt:
			raise AssertionError("Contract failure")

ensures = requires
loop_invariant = ensures
