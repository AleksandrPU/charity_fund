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
            obj_id: int,
            obj_in,
            session: AsyncSession
    ):
        db_obj = await self.get(obj_id, session)
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)

        return db_obj


class DeleteMixin(GetMixin):

    async def remove(
            self,
            obj_id: int,
            session: AsyncSession
    ):
        db_obj = await self.get(obj_id, session)
        await session.delete(db_obj)
        await session.commit()

        return db_obj
