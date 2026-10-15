import httpx


def test_all_imports_are_exported() -> None:
    included_private_members = ["__description__", "__title__", "__version__"]
    # `__all__` is grouped by source module, so membership is what matters.
    assert sorted(httpx.__all__, key=str.casefold) == sorted(
        (
            member
            for member in vars(httpx).keys()
            if not member.startswith("_") or member in included_private_members
        ),
        key=str.casefold,
    )
