from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charityproject import charity_project_crud


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
):
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=422,
            detail=f'Проект с именем {project_name} уже есть.'
        )
