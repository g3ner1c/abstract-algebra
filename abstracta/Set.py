"""
Implementation of Set
"""

from __future__ import annotations


class AlgSet(frozenset):
    """
    Mathematical set object.

    Subclassed from frozenset to add some syntactic sugar and additional methods. Named
    so to avoid confusion with builtin.set and collections.abc.Set

    It's important that AlgSet be a subclass of frozenset, (not set), because:
    1) it makes AlgSet immutable
    2) it allows AlgSet to contains AlgSets
    """

    def __mul__(self, other) -> AlgSet:
        """Cartesian product"""
        if isinstance(other, AlgSet):
            return AlgSet((x, y) for x in self for y in other)
        else:
            return NotImplemented

    # superseed dunder methods to return AlgSet

    def __and__(self, other) -> AlgSet:  # intersection (&)
        return AlgSet(super().__and__(other))

    __rand__ = __and__

    def __or__(self, other) -> AlgSet:  # union (|)
        return AlgSet(super().__or__(other))

    __ror__ = __or__

    def __sub__(self, other) -> AlgSet:  # difference (-)
        return AlgSet(super().__sub__(other))

    def __rsub__(
        self, other
    ) -> AlgSet:  # idk if i actually have to explicitly define this
        return other.__sub__(self)

    def __xor__(self, other) -> AlgSet:  # symmetric difference (^)
        return AlgSet(super().__xor__(other))

    __rxor__ = __xor__

    def pick(self):
        """Return an arbitrary element. (The finite Axiom of Choice is true!)"""

        if len(self) == 0:
            raise KeyError("This is an empty set")

        for item in self:
            break
        return item
