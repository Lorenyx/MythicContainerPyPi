import warnings


def deprecated_property(old_property, new_property) -> None:
    """Emit a warning that the property should not be used anymore"""
    warnings.warn(f"Property '{old_property}' is deprecated and will be removed in a future version."
                  f" Please use '{new_property}' instead.", stacklevel=3)
