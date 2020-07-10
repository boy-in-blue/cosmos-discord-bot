import bson
import arrow
import asyncio
import datetime


class ScheduledTask(object):

    def __init__(self, scheduler, callback, invoke_at, kwargs, created_at=None, _id=None, **_kwargs):
        self.id = _id or bson.ObjectId()
        self.scheduler = scheduler
        self.callback = callback
        self.invoke_at = invoke_at
        self.created_at = created_at or datetime.datetime.utcnow()
        self.kwargs = kwargs

        if self.invoke_at <= self.created_at:
            raise ValueError("The task must be scheduled to future.")

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __call__(self, *args, **kwargs):
        if self.callback.startswith("on_"):
            return self.scheduler.bot.dispatch(self.callback, self, *args, **kwargs, **self.kwargs)

        try:
            object_ = self.scheduler.callbacks[self.callback]
        except KeyError:
            raise ValueError(f"No callback '{self.callback}' is registered yet.")
        else:
            self.scheduler.bot.loop.create_task(object_(self, *args, **kwargs, **self.kwargs))

        self.scheduler.remove_task(self)

    async def dispatch_when_ready(self, *args, **kwargs):
        await asyncio.sleep(self.timedelta.seconds)
        self.__call__(*args, **kwargs)

    @property
    def document(self):
        return {
            "_id": self.id, "callback": self.callback, "invoke_at": self.invoke_at,
            "created_at": self.created_at, "kwargs": dict(self.kwargs),
        }

    @classmethod
    def from_document(cls, scheduler, document):
        return cls(scheduler, **document)

    @property
    def timedelta(self):
        return self.invoke_at - self.created_at

    @property
    def humanize(self):
        return arrow.get(self.invoke_at).humanize()
