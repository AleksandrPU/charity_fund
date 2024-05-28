from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class GetMixin:

    async def get(
            self,
            obj_id: int,
            session: AsyncSession
    ):
        obj = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return obj.scalars().first()


class UpdateMixin(GetMixin):

    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession
    ):
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        # session.add(db_obj)
        # print(f'>>> {db_obj.__dict__=}')
        from app.services.charity_project import CharityProjectService
        await CharityProjectService(session).add_to_queue(db_obj)

        await session.commit()
        await session.refresh(db_obj)
        # print(f'<<< {db_obj.__dict__=}')

        return db_obj


class DeleteMixin(GetMixin):

    async def remove(
            self,
            db_obj,
            session: AsyncSession
    ):
        await session.delete(db_obj)
        await session.commit()

        return db_obj
