import _plotly_utils.basevalidators


class TickmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="tickmode", parent_name="indicator.gauge.axis", **kwargs
    ):
        super(TickmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "linear", "array"]),
            **kwargs
        )
