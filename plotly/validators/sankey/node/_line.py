import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="sankey.node", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color of the `line` around each
                `node`.
            colorsrc
                Sets the source reference on Chart Studio Cloud
                for  color .
            width
                Sets the width (in px) of the `line` around
                each `node`.
            widthsrc
                Sets the source reference on Chart Studio Cloud
                for  width .
""",
            ),
            **kwargs
        )
