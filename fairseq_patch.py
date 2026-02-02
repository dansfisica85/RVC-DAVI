# Wrapper to patch fairseq compatibility with Python 3.12
# This module patches dataclasses to work around the mutable default issue

import sys
from dataclasses import field
from typing import Any, Optional

# Store original field function
_original_field = field

def _patched_field(*, default=None, default_factory=None, **kwargs):
    """Patched field that converts mutable defaults to default_factory"""
    if default is not None and default_factory is None:
        if hasattr(default, '__class__') and default.__class__.__name__ not in ('int', 'str', 'float', 'bool', 'NoneType', 'tuple'):
            # Mutable default detected, convert to factory
            def make_factory(val):
                def factory():
                    import copy
                    return copy.deepcopy(val)
                return factory
            return _original_field(default_factory=make_factory(default), **kwargs)
    return _original_field(default=default, default_factory=default_factory, **kwargs)

# Patch before importing fairseq
import dataclasses
dataclasses.field = _patched_field

# Now import fairseq
try:
    import fairseq.dataclass.configs as configs
except:
    pass

# Restore original field
dataclasses.field = _original_field

# Re-export fairseq modules
from fairseq import checkpoint_utils
from fairseq import utils as fairseq_utils
