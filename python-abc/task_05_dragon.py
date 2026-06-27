#!/usr/bin/env python3


class SwimMixin:
    """Mixin that provides swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swimming and flying abilities."""

    def roar(self):
        print("The dragon roars!")