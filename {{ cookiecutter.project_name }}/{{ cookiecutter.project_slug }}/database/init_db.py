from attrs import define
from sqlalchemy.ext.asyncio import AsyncSession


@define
class InitDbResult:
    """The result of initializing the database."""
    pass


async def init_db(
    session: AsyncSession,
):
    """Initialize the database with minimum required data.

    Args:
        session: The database session.
    """
    import {{ cookiecutter.project_slug }}.database.models.api  # noqa: F401

    with session.no_autoflush:
        # Create the minimum required data.
        pass

    # Save these changes.
    await session.commit()

    # Return records created or retrieved.
    return InitDbResult()
