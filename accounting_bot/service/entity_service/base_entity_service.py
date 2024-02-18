from sqlalchemy.ext.asyncio import AsyncSession


class BaseEntityService:
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

        self.__init__post__()

    def __init__post__(self):
        pass
