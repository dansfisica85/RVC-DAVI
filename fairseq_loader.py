# Workaround module to load fairseq checkpoint_utils without hydra initialization
# This bypasses the dataclass compatibility issues with Python 3.12

import sys
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Prevent hydra initialization by mocking the config store
class MockConfigStore:
    _instance = None
    
    @classmethod
    def instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def store(self, *args, **kwargs):
        pass

# Patch before any imports
sys.modules['hydra.core.config_store'] = type(sys)('mock')
sys.modules['hydra.core.config_store'].ConfigStore = MockConfigStore

# Now we can import fairseq modules more safely
import torch
from collections import OrderedDict

def load_model(hubert_path, device='cpu', is_half=False):
    """Load hubert model without full fairseq initialization"""
    
    # Load checkpoint directly
    checkpoint = torch.load(hubert_path, map_location=device, weights_only=False)
    
    # Try importing fairseq checkpoint utils
    try:
        # This might work with our patches
        from fairseq import checkpoint_utils
        models, _, _ = checkpoint_utils.load_model_ensemble_and_task(
            [hubert_path], suffix=""
        )
        model = models[0].to(device)
    except Exception as e:
        print(f"Note: Using fallback model loading due to: {e}")
        # Fallback - manual loading if available
        raise e
    
    if is_half:
        model = model.half()
    
    model.eval()
    return model

# Export what's needed
__all__ = ['load_model']
