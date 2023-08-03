class Director:
    """Director is responsible for the construction process."""

    def __init__(self, builder):
        self._builder = builder

    def construct_basic_vehicle(self):
        self._builder.build_body()
        self._builder.install_engine()
        self._builder.paint_vehicle()

    def get_vehicle(self):
        return self._builder.get_vehicle()
