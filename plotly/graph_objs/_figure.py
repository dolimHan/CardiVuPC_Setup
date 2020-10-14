from plotly.basedatatypes import BaseFigure


class Figure(BaseFigure):
    def __init__(
        self, data=None, layout=None, frames=None, skip_invalid=False, **kwargs
    ):
        """
        Create a new :class:Figure instance
        
        Parameters
        ----------
        data
            The 'data' property is a tuple of trace instances
            that may be specified as:
              - A list or tuple of trace instances
                (e.g. [Scatter(...), Bar(...)])
              - A single trace instance
                (e.g. Scatter(...), Bar(...), etc.)
              - A list or tuple of dicts of string/value properties where:
                - The 'type' property specifies the trace type
                    One of: ['area', 'bar', 'barpolar', 'box',
                             'candlestick', 'carpet', 'choropleth',
                             'choroplethmapbox', 'cone', 'contour',
                             'contourcarpet', 'densitymapbox', 'funnel',
                             'funnelarea', 'heatmap', 'heatmapgl',
                             'histogram', 'histogram2d',
                             'histogram2dcontour', 'image', 'indicator',
                             'isosurface', 'mesh3d', 'ohlc', 'parcats',
                             'parcoords', 'pie', 'pointcloud', 'sankey',
                             'scatter', 'scatter3d', 'scattercarpet',
                             'scattergeo', 'scattergl', 'scattermapbox',
                             'scatterpolar', 'scatterpolargl',
                             'scatterternary', 'splom', 'streamtube',
                             'sunburst', 'surface', 'table', 'treemap',
                             'violin', 'volume', 'waterfall']
        
                - All remaining properties are passed to the constructor of
                  the specified trace type
        
                (e.g. [{'type': 'scatter', ...}, {'type': 'bar, ...}])
            
        layout
            The 'layout' property is an instance of Layout
            that may be specified as:
              - An instance of :class:`plotly.graph_objs.Layout`
              - A dict of string/value properties that will be passed
                to the Layout constructor
        
                Supported dict properties:
                    
                    activeshape
                        :class:`plotly.graph_objects.layout.Activeshape
                        ` instance or dict with compatible properties
                    angularaxis
                        :class:`plotly.graph_objects.layout.AngularAxis
                        ` instance or dict with compatible properties
                    annotations
                        A tuple of
                        :class:`plotly.graph_objects.layout.Annotation`
                        instances or dicts with compatible properties
                    annotationdefaults
                        When used in a template (as
                        layout.template.layout.annotationdefaults),
                        sets the default property values to use for
                        elements of layout.annotations
                    autosize
                        Determines whether or not a layout width or
                        height that has been left undefined by the user
                        is initialized on each relayout. Note that,
                        regardless of this attribute, an undefined
                        layout width or height is always initialized on
                        the first call to plot.
                    bargap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    bargroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    barmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "stack", the bars are stacked on top of one
                        another With "relative", the bars are stacked
                        on top of one another, with negative values
                        below the axis, positive values above With
                        "group", the bars are plotted next to one
                        another centered around the shared location.
                        With "overlay", the bars are plotted over one
                        another, you might need to an "opacity" to see
                        multiple bars.
                    barnorm
                        Sets the normalization for bar traces on the
                        graph. With "fraction", the value of each bar
                        is divided by the sum of all values at that
                        location coordinate. "percent" is the same but
                        multiplied by 100 to show percentages.
                    boxgap
                        Sets the gap (in plot fraction) between boxes
                        of adjacent location coordinates. Has no effect
                        on traces that have "width" set.
                    boxgroupgap
                        Sets the gap (in plot fraction) between boxes
                        of the same location coordinate. Has no effect
                        on traces that have "width" set.
                    boxmode
                        Determines how boxes at the same location
                        coordinate are displayed on the graph. If
                        "group", the boxes are plotted next to one
                        another centered around the shared location. If
                        "overlay", the boxes are plotted over one
                        another, you might need to set "opacity" to see
                        them multiple boxes. Has no effect on traces
                        that have "width" set.
                    calendar
                        Sets the default calendar system to use for
                        interpreting and displaying dates throughout
                        the plot.
                    clickmode
                        Determines the mode of single click
                        interactions. "event" is the default value and
                        emits the `plotly_click` event. In addition
                        this mode emits the `plotly_selected` event in
                        drag modes "lasso" and "select", but with no
                        event data attached (kept for compatibility
                        reasons). The "select" flag enables selecting
                        single data points via click. This mode also
                        supports persistent selections, meaning that
                        pressing Shift while clicking, adds to /
                        subtracts from an existing selection. "select"
                        with `hovermode`: "x" can be confusing,
                        consider explicitly setting `hovermode`:
                        "closest" when using this feature. Selection
                        events are sent accordingly as long as "event"
                        flag is set as well. When the "event" flag is
                        missing, `plotly_click` and `plotly_selected`
                        events are not fired.
                    coloraxis
                        :class:`plotly.graph_objects.layout.Coloraxis`
                        instance or dict with compatible properties
                    colorscale
                        :class:`plotly.graph_objects.layout.Colorscale`
                        instance or dict with compatible properties
                    colorway
                        Sets the default trace colors.
                    datarevision
                        If provided, a changed value tells
                        `Plotly.react` that one or more data arrays has
                        changed. This way you can modify arrays in-
                        place rather than making a complete new copy
                        for an incremental change. If NOT provided,
                        `Plotly.react` assumes that data arrays are
                        being treated as immutable, thus any data array
                        with a different identity from its predecessor
                        contains new data.
                    direction
                        Legacy polar charts are deprecated! Please
                        switch to "polar" subplots. Sets the direction
                        corresponding to positive angles in legacy
                        polar charts.
                    dragmode
                        Determines the mode of drag interactions.
                        "select" and "lasso" apply only to scatter
                        traces with markers or text. "orbit" and
                        "turntable" apply only to 3D scenes.
                    editrevision
                        Controls persistence of user-driven changes in
                        `editable: true` configuration, other than
                        trace names and axis titles. Defaults to
                        `layout.uirevision`.
                    extendfunnelareacolors
                        If `true`, the funnelarea slice colors (whether
                        given by `funnelareacolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendpiecolors
                        If `true`, the pie slice colors (whether given
                        by `piecolorway` or inherited from `colorway`)
                        will be extended to three times its original
                        length by first repeating every color 20%
                        lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendsunburstcolors
                        If `true`, the sunburst slice colors (whether
                        given by `sunburstcolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendtreemapcolors
                        If `true`, the treemap slice colors (whether
                        given by `treemapcolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    font
                        Sets the global font. Note that fonts used in
                        traces and other layout components inherit from
                        the global font.
                    funnelareacolorway
                        Sets the default funnelarea slice colors.
                        Defaults to the main `colorway` used for trace
                        colors. If you specify a new list here it can
                        still be extended with lighter and darker
                        colors, see `extendfunnelareacolors`.
                    funnelgap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    funnelgroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    funnelmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "stack", the bars are stacked on top of one
                        another With "group", the bars are plotted next
                        to one another centered around the shared
                        location. With "overlay", the bars are plotted
                        over one another, you might need to an
                        "opacity" to see multiple bars.
                    geo
                        :class:`plotly.graph_objects.layout.Geo`
                        instance or dict with compatible properties
                    grid
                        :class:`plotly.graph_objects.layout.Grid`
                        instance or dict with compatible properties
                    height
                        Sets the plot's height (in px).
                    hiddenlabels
                        hiddenlabels is the funnelarea & pie chart
                        analog of visible:'legendonly' but it can
                        contain many labels, and can simultaneously
                        hide slices from several pies/funnelarea charts
                    hiddenlabelssrc
                        Sets the source reference on Chart Studio Cloud
                        for  hiddenlabels .
                    hidesources
                        Determines whether or not a text link citing
                        the data source is placed at the bottom-right
                        cored of the figure. Has only an effect only on
                        graphs that have been generated via forked
                        graphs from the Chart Studio Cloud (at
                        https://chart-studio.plotly.com or on-premise).
                    hoverdistance
                        Sets the default distance (in pixels) to look
                        for data to add hover labels (-1 means no
                        cutoff, 0 means no looking for data). This is
                        only a real distance for hovering on point-like
                        objects, like scatter points. For area-like
                        objects (bars, scatter fills, etc) hovering is
                        on inside the area and off outside, but these
                        objects will not supersede hover on point-like
                        objects in case of conflict.
                    hoverlabel
                        :class:`plotly.graph_objects.layout.Hoverlabel`
                        instance or dict with compatible properties
                    hovermode
                        Determines the mode of hover interactions. If
                        "closest", a single hoverlabel will appear for
                        the "closest" point within the `hoverdistance`.
                        If "x" (or "y"), multiple hoverlabels will
                        appear for multiple points at the "closest" x-
                        (or y-) coordinate within the `hoverdistance`,
                        with the caveat that no more than one
                        hoverlabel will appear per trace. If *x
                        unified* (or *y unified*), a single hoverlabel
                        will appear multiple points at the closest x-
                        (or y-) coordinate within the `hoverdistance`
                        with the caveat that no more than one
                        hoverlabel will appear per trace. In this mode,
                        spikelines are enabled by default perpendicular
                        to the specified axis. If false, hover
                        interactions are disabled. If `clickmode`
                        includes the "select" flag, `hovermode`
                        defaults to "closest". If `clickmode` lacks the
                        "select" flag, it defaults to "x" or "y"
                        (depending on the trace's `orientation` value)
                        for plots based on cartesian coordinates. For
                        anything else the default value is "closest".
                    images
                        A tuple of
                        :class:`plotly.graph_objects.layout.Image`
                        instances or dicts with compatible properties
                    imagedefaults
                        When used in a template (as
                        layout.template.layout.imagedefaults), sets the
                        default property values to use for elements of
                        layout.images
                    legend
                        :class:`plotly.graph_objects.layout.Legend`
                        instance or dict with compatible properties
                    mapbox
                        :class:`plotly.graph_objects.layout.Mapbox`
                        instance or dict with compatible properties
                    margin
                        :class:`plotly.graph_objects.layout.Margin`
                        instance or dict with compatible properties
                    meta
                        Assigns extra meta information that can be used
                        in various `text` attributes. Attributes such
                        as the graph, axis and colorbar `title.text`,
                        annotation `text` `trace.name` in legend items,
                        `rangeselector`, `updatemenus` and `sliders`
                        `label` text all support `meta`. One can access
                        `meta` fields using template strings:
                        `%{meta[i]}` where `i` is the index of the
                        `meta` item in question. `meta` can also be an
                        object for example `{key: value}` which can be
                        accessed %{meta[key]}.
                    metasrc
                        Sets the source reference on Chart Studio Cloud
                        for  meta .
                    modebar
                        :class:`plotly.graph_objects.layout.Modebar`
                        instance or dict with compatible properties
                    newshape
                        :class:`plotly.graph_objects.layout.Newshape`
                        instance or dict with compatible properties
                    orientation
                        Legacy polar charts are deprecated! Please
                        switch to "polar" subplots. Rotates the entire
                        polar by the given angle in legacy polar
                        charts.
                    paper_bgcolor
                        Sets the background color of the paper where
                        the graph is drawn.
                    piecolorway
                        Sets the default pie slice colors. Defaults to
                        the main `colorway` used for trace colors. If
                        you specify a new list here it can still be
                        extended with lighter and darker colors, see
                        `extendpiecolors`.
                    plot_bgcolor
                        Sets the background color of the plotting area
                        in-between x and y axes.
                    polar
                        :class:`plotly.graph_objects.layout.Polar`
                        instance or dict with compatible properties
                    radialaxis
                        :class:`plotly.graph_objects.layout.RadialAxis`
                        instance or dict with compatible properties
                    scene
                        :class:`plotly.graph_objects.layout.Scene`
                        instance or dict with compatible properties
                    selectdirection
                        When `dragmode` is set to "select", this limits
                        the selection of the drag to horizontal,
                        vertical or diagonal. "h" only allows
                        horizontal selection, "v" only vertical, "d"
                        only diagonal and "any" sets no limit.
                    selectionrevision
                        Controls persistence of user-driven changes in
                        selected points from all traces.
                    separators
                        Sets the decimal and thousand separators. For
                        example, *. * puts a '.' before decimals and a
                        space between thousands. In English locales,
                        dflt is ".," but other locales may alter this
                        default.
                    shapes
                        A tuple of
                        :class:`plotly.graph_objects.layout.Shape`
                        instances or dicts with compatible properties
                    shapedefaults
                        When used in a template (as
                        layout.template.layout.shapedefaults), sets the
                        default property values to use for elements of
                        layout.shapes
                    showlegend
                        Determines whether or not a legend is drawn.
                        Default is `true` if there is a trace to show
                        and any of these: a) Two or more traces would
                        by default be shown in the legend. b) One pie
                        trace is shown in the legend. c) One trace is
                        explicitly given with `showlegend: true`.
                    sliders
                        A tuple of
                        :class:`plotly.graph_objects.layout.Slider`
                        instances or dicts with compatible properties
                    sliderdefaults
                        When used in a template (as
                        layout.template.layout.sliderdefaults), sets
                        the default property values to use for elements
                        of layout.sliders
                    spikedistance
                        Sets the default distance (in pixels) to look
                        for data to draw spikelines to (-1 means no
                        cutoff, 0 means no looking for data). As with
                        hoverdistance, distance does not apply to area-
                        like objects. In addition, some objects can be
                        hovered on but will not generate spikelines,
                        such as scatter fills.
                    sunburstcolorway
                        Sets the default sunburst slice colors.
                        Defaults to the main `colorway` used for trace
                        colors. If you specify a new list here it can
                        still be extended with lighter and darker
                        colors, see `extendsunburstcolors`.
                    template
                        Default attributes to be applied to the plot.
                        This should be a dict with format: `{'layout':
                        layoutTemplate, 'data': {trace_type:
                        [traceTemplate, ...], ...}}` where
                        `layoutTemplate` is a dict matching the
                        structure of `figure.layout` and
                        `traceTemplate` is a dict matching the
                        structure of the trace with type `trace_type`
                        (e.g. 'scatter'). Alternatively, this may be
                        specified as an instance of
                        plotly.graph_objs.layout.Template.  Trace
                        templates are applied cyclically to traces of
                        each type. Container arrays (eg `annotations`)
                        have special handling: An object ending in
                        `defaults` (eg `annotationdefaults`) is applied
                        to each array item. But if an item has a
                        `templateitemname` key we look in the template
                        array for an item with matching `name` and
                        apply that instead. If no matching `name` is
                        found we mark the item invisible. Any named
                        template item not referenced is appended to the
                        end of the array, so this can be used to add a
                        watermark annotation or a logo image, for
                        example. To omit one of these items on the
                        plot, make an item with matching
                        `templateitemname` and `visible: false`.
                    ternary
                        :class:`plotly.graph_objects.layout.Ternary`
                        instance or dict with compatible properties
                    title
                        :class:`plotly.graph_objects.layout.Title`
                        instance or dict with compatible properties
                    titlefont
                        Deprecated: Please use layout.title.font
                        instead. Sets the title font. Note that the
                        title's font used to be customized by the now
                        deprecated `titlefont` attribute.
                    transition
                        Sets transition options used during
                        Plotly.react updates.
                    treemapcolorway
                        Sets the default treemap slice colors. Defaults
                        to the main `colorway` used for trace colors.
                        If you specify a new list here it can still be
                        extended with lighter and darker colors, see
                        `extendtreemapcolors`.
                    uirevision
                        Used to allow user interactions with the plot
                        to persist after `Plotly.react` calls that are
                        unaware of these interactions. If `uirevision`
                        is omitted, or if it is given and it changed
                        from the previous `Plotly.react` call, the
                        exact new figure is used. If `uirevision` is
                        truthy and did NOT change, any attribute that
                        has been affected by user interactions and did
                        not receive a different value in the new figure
                        will keep the interaction value.
                        `layout.uirevision` attribute serves as the
                        default for `uirevision` attributes in various
                        sub-containers. For finer control you can set
                        these sub-attributes directly. For example, if
                        your app separately controls the data on the x
                        and y axes you might set
                        `xaxis.uirevision=*time*` and
                        `yaxis.uirevision=*cost*`. Then if only the y
                        data is changed, you can update
                        `yaxis.uirevision=*quantity*` and the y axis
                        range will reset but the x axis range will
                        retain any user-driven zoom.
                    uniformtext
                        :class:`plotly.graph_objects.layout.Uniformtext
                        ` instance or dict with compatible properties
                    updatemenus
                        A tuple of
                        :class:`plotly.graph_objects.layout.Updatemenu`
                        instances or dicts with compatible properties
                    updatemenudefaults
                        When used in a template (as
                        layout.template.layout.updatemenudefaults),
                        sets the default property values to use for
                        elements of layout.updatemenus
                    violingap
                        Sets the gap (in plot fraction) between violins
                        of adjacent location coordinates. Has no effect
                        on traces that have "width" set.
                    violingroupgap
                        Sets the gap (in plot fraction) between violins
                        of the same location coordinate. Has no effect
                        on traces that have "width" set.
                    violinmode
                        Determines how violins at the same location
                        coordinate are displayed on the graph. If
                        "group", the violins are plotted next to one
                        another centered around the shared location. If
                        "overlay", the violins are plotted over one
                        another, you might need to set "opacity" to see
                        them multiple violins. Has no effect on traces
                        that have "width" set.
                    waterfallgap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    waterfallgroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    waterfallmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "group", the bars are plotted next to one
                        another centered around the shared location.
                        With "overlay", the bars are plotted over one
                        another, you might need to an "opacity" to see
                        multiple bars.
                    width
                        Sets the plot's width (in px).
                    xaxis
                        :class:`plotly.graph_objects.layout.XAxis`
                        instance or dict with compatible properties
                    yaxis
                        :class:`plotly.graph_objects.layout.YAxis`
                        instance or dict with compatible properties
            
        frames
            The 'frames' property is a tuple of instances of
            Frame that may be specified as:
              - A list or tuple of instances of plotly.graph_objs.Frame
              - A list or tuple of dicts of string/value properties that
                will be passed to the Frame constructor
        
                Supported dict properties:
                    
                    baseframe
                        The name of the frame into which this frame's
                        properties are merged before applying. This is
                        used to unify properties and avoid needing to
                        specify the same values for the same properties
                        in multiple frames.
                    data
                        A list of traces this frame modifies. The
                        format is identical to the normal trace
                        definition.
                    group
                        An identifier that specifies the group to which
                        the frame belongs, used by animate to select a
                        subset of frames.
                    layout
                        Layout properties which this frame modifies.
                        The format is identical to the normal layout
                        definition.
                    name
                        A label by which to identify the frame
                    traces
                        A list of trace indices that identify the
                        respective traces in the data attribute
            
        skip_invalid: bool
            If True, invalid properties in the figure specification will be
            skipped silently. If False (default) invalid properties in the
            figure specification will result in a ValueError

        Raises
        ------
        ValueError
            if a property in the specification of data, layout, or frames
            is invalid AND skip_invalid is False
        """
        super(Figure, self).__init__(data, layout, frames, skip_invalid, **kwargs)

    def add_area(
        self,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        r=None,
        rsrc=None,
        showlegend=None,
        stream=None,
        t=None,
        tsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Area trace
        
        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.area.Hoverlabel` instance
            or dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.area.Marker` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the radial coordinates for
            legacy polar chart only.
        rsrc
            Sets the source reference on Chart Studio Cloud for  r
            .
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.area.Stream` instance or
            dict with compatible properties
        t
            Area traces are deprecated! Please switch to the
            "barpolar" trace type. Sets the angular coordinates for
            legacy polar chart only.
        tsrc
            Sets the source reference on Chart Studio Cloud for  t
            .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Area

        new_trace = Area(
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            r=r,
            rsrc=rsrc,
            showlegend=showlegend,
            stream=stream,
            t=t,
            tsrc=tsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_bar(
        self,
        alignmentgroup=None,
        base=None,
        basesrc=None,
        cliponaxis=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        offsetsrc=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        r=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        t=None,
        text=None,
        textangle=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        tsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        widthsrc=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Bar trace
        
        The data visualized by the span of the bars is set in `y` if
        `orientation` is set th "v" (the default) and the labels are
        set in `x`. By setting `orientation` to "h", the roles are
        interchanged.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        base
            Sets where the bar base is drawn (in position axis
            units). In "stack" or "relative" barmode, traces that
            set "base" will be excluded and drawn in "overlay" mode
            instead.
        basesrc
            Sets the source reference on Chart Studio Cloud for
            base .
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            :class:`plotly.graph_objects.bar.ErrorX` instance or
            dict with compatible properties
        error_y
            :class:`plotly.graph_objects.bar.ErrorY` instance or
            dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.bar.Hoverlabel` instance
            or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `value` and `label`. Anything
            contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        insidetextanchor
            Determines if texts are kept at center or start/end
            points in `textposition` "inside" mode.
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.bar.Marker` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        offsetsrc
            Sets the source reference on Chart Studio Cloud for
            offset .
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        r
            r coordinates in scatter traces are deprecated!Please
            switch to the "scatterpolar" trace type.Sets the radial
            coordinatesfor legacy polar chart only.
        rsrc
            Sets the source reference on Chart Studio Cloud for  r
            .
        selected
            :class:`plotly.graph_objects.bar.Selected` instance or
            dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.bar.Stream` instance or
            dict with compatible properties
        t
            t coordinates in scatter traces are deprecated!Please
            switch to the "scatterpolar" trace type.Sets the
            angular coordinatesfor legacy polar chart only.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textangle
            Sets the angle of the tick labels with respect to the
            bar. For example, a `tickangle` of -90 draws the tick
            labels vertically. With "auto" the texts may
            automatically be rotated to fit with the maximum size
            in bars.
        textfont
            Sets the font used for `text`.
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed), unless
            there is another bar stacked on this one, then the text
            gets pushed inside. "auto" tries to position `text`
            inside the bar, but if the bar is too small and no bar
            is stacked on this one the text is moved outside.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `value` and
            `label`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        tsrc
            Sets the source reference on Chart Studio Cloud for  t
            .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.bar.Unselected` instance
            or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        widthsrc
            Sets the source reference on Chart Studio Cloud for
            width .
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Bar

        new_trace = Bar(
            alignmentgroup=alignmentgroup,
            base=base,
            basesrc=basesrc,
            cliponaxis=cliponaxis,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            offsetsrc=offsetsrc,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            r=r,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            t=t,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            tsrc=tsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_barpolar(
        self,
        base=None,
        basesrc=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetsrc=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        widthsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Barpolar trace
        
        The data visualized by the radial span of the bars is set in
        `r`

        Parameters
        ----------
        base
            Sets where the bar base is drawn (in radial axis
            units). In "stack" barmode, traces that set "base" will
            be excluded and drawn in "overlay" mode instead.
        basesrc
            Sets the source reference on Chart Studio Cloud for
            base .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.barpolar.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.barpolar.Marker` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the angular position where the bar is drawn (in
            "thetatunit" units).
        offsetsrc
            Sets the source reference on Chart Studio Cloud for
            offset .
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on Chart Studio Cloud for  r
            .
        selected
            :class:`plotly.graph_objects.barpolar.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.barpolar.Stream` instance
            or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets hover text elements associated with each bar. If a
            single string, the same string appears over all bars.
            If an array of string, the items are mapped in order to
            the this trace's coordinates.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on Chart Studio Cloud for
            theta .
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.barpolar.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar angular width (in "thetaunit" units).
        widthsrc
            Sets the source reference on Chart Studio Cloud for
            width .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Barpolar

        new_trace = Barpolar(
            base=base,
            basesrc=basesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetsrc=offsetsrc,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_box(
        self,
        alignmentgroup=None,
        boxmean=None,
        boxpoints=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        jitter=None,
        legendgroup=None,
        line=None,
        lowerfence=None,
        lowerfencesrc=None,
        marker=None,
        mean=None,
        meansrc=None,
        median=None,
        mediansrc=None,
        meta=None,
        metasrc=None,
        name=None,
        notched=None,
        notchspan=None,
        notchspansrc=None,
        notchwidth=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        pointpos=None,
        q1=None,
        q1src=None,
        q3=None,
        q3src=None,
        quartilemethod=None,
        sd=None,
        sdsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        upperfence=None,
        upperfencesrc=None,
        visible=None,
        whiskerwidth=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Box trace
        
        Each box spans from quartile 1 (Q1) to quartile 3 (Q3). The
        second quartile (Q2, i.e. the median) is marked by a line
        inside the box. The fences grow outward from the boxes' edges,
        by default they span +/- 1.5 times the interquartile range
        (IQR: Q3-Q1), The sample mean and standard deviation as well as
        notches and the sample, outlier and suspected outliers points
        can be optionally added to the box plot. The values and
        positions corresponding to each boxes can be input using two
        signatures. The first signature expects users to supply the
        sample values in the `y` data array for vertical boxes (`x` for
        horizontal boxes). By supplying an `x` (`y`) array, one box per
        distinct `x` (`y`) value is drawn If no `x` (`y`) list is
        provided, a single box is drawn. In this case, the box is
        positioned with the trace `name` or with `x0` (`y0`) if
        provided. The second signature expects users to supply the
        boxes corresponding Q1, median and Q3 statistics in the `q1`,
        `median` and `q3` data arrays respectively. Other box features
        relying on statistics namely `lowerfence`, `upperfence`,
        `notchspan` can be set directly by the users. To have plotly
        compute them or to show sample points besides the boxes, users
        can set the `y` data array for vertical boxes (`x` for
        horizontal boxes) to a 2D array with the outer length
        corresponding to the number of boxes in the traces and the
        inner length corresponding the sample size.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        boxmean
            If True, the mean of the box(es)' underlying
            distribution is drawn as a dashed line inside the
            box(es). If "sd" the standard deviation is also drawn.
            Defaults to True when `mean` is set. Defaults to "sd"
            when `sd` is set Otherwise defaults to False.
        boxpoints
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the box(es) are shown with no sample
            points Defaults to "suspectedoutliers" when
            `marker.outliercolor` or `marker.line.outliercolor` is
            set. Defaults to "all" under the q1/median/q3
            signature. Otherwise defaults to "outliers".
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Sets the x coordinate step for multi-box traces set
            using q1/median/q3.
        dy
            Sets the y coordinate step for multi-box traces set
            using q1/median/q3.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.box.Hoverlabel` instance
            or dict with compatible properties
        hoveron
            Do the hover effects highlight individual boxes  or
            sample points or both?
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        jitter
            Sets the amount of jitter in the sample points drawn.
            If 0, the sample points align along the distribution
            axis. If 1, the sample points are drawn in a random
            jitter of width equal to the width of the box(es).
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.box.Line` instance or dict
            with compatible properties
        lowerfence
            Sets the lower fence values. There should be as many
            items as the number of boxes desired. This attribute
            has effect only under the q1/median/q3 signature. If
            `lowerfence` is not provided but a sample (in `y` or
            `x`) is set, we compute the lower as the last sample
            point below 1.5 times the IQR.
        lowerfencesrc
            Sets the source reference on Chart Studio Cloud for
            lowerfence .
        marker
            :class:`plotly.graph_objects.box.Marker` instance or
            dict with compatible properties
        mean
            Sets the mean values. There should be as many items as
            the number of boxes desired. This attribute has effect
            only under the q1/median/q3 signature. If `mean` is not
            provided but a sample (in `y` or `x`) is set, we
            compute the mean for each box using the sample values.
        meansrc
            Sets the source reference on Chart Studio Cloud for
            mean .
        median
            Sets the median values. There should be as many items
            as the number of boxes desired.
        mediansrc
            Sets the source reference on Chart Studio Cloud for
            median .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover. For box traces, the name will
            also be used for the position coordinate, if `x` and
            `x0` (`y` and `y0` if horizontal) are missing and the
            position axis is categorical
        notched
            Determines whether or not notches are drawn. Notches
            displays a confidence interval around the median. We
            compute the confidence interval as median +/- 1.57 *
            IQR / sqrt(N), where IQR is the interquartile range and
            N is the sample size. If two boxes' notches do not
            overlap there is 95% confidence their medians differ.
            See https://sites.google.com/site/davidsstatistics/home
            /notched-box-plots for more info. Defaults to False
            unless `notchwidth` or `notchspan` is set.
        notchspan
            Sets the notch span from the boxes' `median` values.
            There should be as many items as the number of boxes
            desired. This attribute has effect only under the
            q1/median/q3 signature. If `notchspan` is not provided
            but a sample (in `y` or `x`) is set, we compute it as
            1.57 * IQR / sqrt(N), where N is the sample size.
        notchspansrc
            Sets the source reference on Chart Studio Cloud for
            notchspan .
        notchwidth
            Sets the width of the notches relative to the box'
            width. For example, with 0, the notches are as wide as
            the box(es).
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the box(es). If "v" ("h"), the
            distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the box(es). If 0, the sample points are places over
            the center of the box(es). Positive (negative) values
            correspond to positions to the right (left) for
            vertical boxes and above (below) for horizontal boxes
        q1
            Sets the Quartile 1 values. There should be as many
            items as the number of boxes desired.
        q1src
            Sets the source reference on Chart Studio Cloud for  q1
            .
        q3
            Sets the Quartile 3 values. There should be as many
            items as the number of boxes desired.
        q3src
            Sets the source reference on Chart Studio Cloud for  q3
            .
        quartilemethod
            Sets the method used to compute the sample's Q1 and Q3
            quartiles. The "linear" method uses the 25th percentile
            for Q1 and 75th percentile for Q3 as computed using
            method #10 (listed on http://www.amstat.org/publication
            s/jse/v14n3/langford.html). The "exclusive" method uses
            the median to divide the ordered dataset into two
            halves if the sample is odd, it does not include the
            median in either half - Q1 is then the median of the
            lower half and Q3 the median of the upper half. The
            "inclusive" method also uses the median to divide the
            ordered dataset into two halves but if the sample is
            odd, it includes the median in both halves - Q1 is then
            the median of the lower half and Q3 the median of the
            upper half.
        sd
            Sets the standard deviation values. There should be as
            many items as the number of boxes desired. This
            attribute has effect only under the q1/median/q3
            signature. If `sd` is not provided but a sample (in `y`
            or `x`) is set, we compute the standard deviation for
            each box using the sample values.
        sdsrc
            Sets the source reference on Chart Studio Cloud for  sd
            .
        selected
            :class:`plotly.graph_objects.box.Selected` instance or
            dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.box.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with each sample
            value. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.box.Unselected` instance
            or dict with compatible properties
        upperfence
            Sets the upper fence values. There should be as many
            items as the number of boxes desired. This attribute
            has effect only under the q1/median/q3 signature. If
            `upperfence` is not provided but a sample (in `y` or
            `x`) is set, we compute the lower as the last sample
            point above 1.5 times the IQR.
        upperfencesrc
            Sets the source reference on Chart Studio Cloud for
            upperfence .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        whiskerwidth
            Sets the width of the whiskers relative to the box'
            width. For example, with 1, the whiskers are as wide as
            the box(es).
        width
            Sets the width of the box in data coordinate If 0
            (default value) the width is automatically selected
            based on the positions of other box traces in the same
            subplot.
        x
            Sets the x sample data or coordinates. See overview for
            more info.
        x0
            Sets the x coordinate for single-box traces or the
            starting coordinate for multi-box traces set using
            q1/median/q3. See overview for more info.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y sample data or coordinates. See overview for
            more info.
        y0
            Sets the y coordinate for single-box traces or the
            starting coordinate for multi-box traces set using
            q1/median/q3. See overview for more info.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Box

        new_trace = Box(
            alignmentgroup=alignmentgroup,
            boxmean=boxmean,
            boxpoints=boxpoints,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            jitter=jitter,
            legendgroup=legendgroup,
            line=line,
            lowerfence=lowerfence,
            lowerfencesrc=lowerfencesrc,
            marker=marker,
            mean=mean,
            meansrc=meansrc,
            median=median,
            mediansrc=mediansrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            notched=notched,
            notchspan=notchspan,
            notchspansrc=notchspansrc,
            notchwidth=notchwidth,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            pointpos=pointpos,
            q1=q1,
            q1src=q1src,
            q3=q3,
            q3src=q3src,
            quartilemethod=quartilemethod,
            sd=sd,
            sdsrc=sdsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            upperfence=upperfence,
            upperfencesrc=upperfencesrc,
            visible=visible,
            whiskerwidth=whiskerwidth,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_candlestick(
        self,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legendgroup=None,
        line=None,
        low=None,
        lowsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        whiskerwidth=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        yaxis=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Candlestick trace
        
        The candlestick is a style of financial chart describing open,
        high, low and close for a given `x` coordinate (most likely
        time). The boxes represent the spread between the `open` and
        `close` values and the lines represent the spread between the
        `low` and `high` values Sample points where the close value is
        higher (lower) then the open value are called increasing
        (decreasing). By default, increasing candles are drawn in green
        whereas decreasing are drawn in red.

        Parameters
        ----------
        close
            Sets the close values.
        closesrc
            Sets the source reference on Chart Studio Cloud for
            close .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        decreasing
            :class:`plotly.graph_objects.candlestick.Decreasing`
            instance or dict with compatible properties
        high
            Sets the high values.
        highsrc
            Sets the source reference on Chart Studio Cloud for
            high .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.candlestick.Hoverlabel`
            instance or dict with compatible properties
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        increasing
            :class:`plotly.graph_objects.candlestick.Increasing`
            instance or dict with compatible properties
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.candlestick.Line` instance
            or dict with compatible properties
        low
            Sets the low values.
        lowsrc
            Sets the source reference on Chart Studio Cloud for
            low .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        open
            Sets the open values.
        opensrc
            Sets the source reference on Chart Studio Cloud for
            open .
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.candlestick.Stream`
            instance or dict with compatible properties
        text
            Sets hover text elements associated with each sample
            point. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to this trace's sample points.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        whiskerwidth
            Sets the width of the whiskers relative to the box'
            width. For example, with 1, the whiskers are as wide as
            the box(es).
        x
            Sets the x coordinates. If absent, linear coordinate
            will be generated.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Candlestick

        new_trace = Candlestick(
            close=close,
            closesrc=closesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            high=high,
            highsrc=highsrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            legendgroup=legendgroup,
            line=line,
            low=low,
            lowsrc=lowsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            open=open,
            opensrc=opensrc,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            whiskerwidth=whiskerwidth,
            x=x,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            yaxis=yaxis,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_carpet(
        self,
        a=None,
        a0=None,
        aaxis=None,
        asrc=None,
        b=None,
        b0=None,
        baxis=None,
        bsrc=None,
        carpet=None,
        cheaterslope=None,
        color=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        font=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Carpet trace
        
        The data describing carpet axis layout is set in `y` and
        (optionally) also `x`. If only `y` is present, `x` the plot is
        interpreted as a cheater plot and is filled in using the `y`
        values. `x` and `y` may either be 2D arrays matching with each
        dimension matching that of `a` and `b`, or they may be 1D
        arrays with total length equal to that of `a` and `b`.

        Parameters
        ----------
        a
            An array containing values of the first parameter value
        a0
            Alternate to `a`. Builds a linear space of a
            coordinates. Use with `da` where `a0` is the starting
            coordinate and `da` the step.
        aaxis
            :class:`plotly.graph_objects.carpet.Aaxis` instance or
            dict with compatible properties
        asrc
            Sets the source reference on Chart Studio Cloud for  a
            .
        b
            A two dimensional array of y coordinates at each carpet
            point.
        b0
            Alternate to `b`. Builds a linear space of a
            coordinates. Use with `db` where `b0` is the starting
            coordinate and `db` the step.
        baxis
            :class:`plotly.graph_objects.carpet.Baxis` instance or
            dict with compatible properties
        bsrc
            Sets the source reference on Chart Studio Cloud for  b
            .
        carpet
            An identifier for this carpet, so that `scattercarpet`
            and `contourcarpet` traces can specify a carpet plot on
            which they lie
        cheaterslope
            The shift applied to each successive row of data in
            creating a cheater plot. Only used if `x` is been
            ommitted.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        da
            Sets the a coordinate step. See `a0` for more info.
        db
            Sets the b coordinate step. See `b0` for more info.
        font
            The default font used for axis & tick labels on this
            carpet
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        stream
            :class:`plotly.graph_objects.carpet.Stream` instance or
            dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            A two dimensional array of x coordinates at each carpet
            point. If ommitted, the plot is a cheater plot and the
            xaxis is hidden by default.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            A two dimensional array of y coordinates at each carpet
            point.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Carpet

        new_trace = Carpet(
            a=a,
            a0=a0,
            aaxis=aaxis,
            asrc=asrc,
            b=b,
            b0=b0,
            baxis=baxis,
            bsrc=bsrc,
            carpet=carpet,
            cheaterslope=cheaterslope,
            color=color,
            customdata=customdata,
            customdatasrc=customdatasrc,
            da=da,
            db=db,
            font=font,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_choropleth(
        self,
        autocolorscale=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        featureidkey=None,
        geo=None,
        geojson=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        locationmode=None,
        locations=None,
        locationssrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        reversescale=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Choropleth trace
        
        The data that describes the choropleth value-to-color mapping
        is set in `z`. The geographic locations corresponding to each
        value in `z` are set in `locations`.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.choropleth.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        featureidkey
            Sets the key in GeoJSON features which is used as id to
            match the items included in the `locations` array. Only
            has an effect when `geojson` is set. Support nested
            property, for example "properties.name".
        geo
            Sets a reference between this trace's geospatial
            coordinates and a geographic map. If "geo" (the default
            value), the geospatial coordinates refer to
            `layout.geo`. If "geo2", the geospatial coordinates
            refer to `layout.geo2`, and so on.
        geojson
            Sets optional GeoJSON data associated with this trace.
            If not given, the features on the base map are used. It
            can be set as a valid GeoJSON object or as a URL
            string. Note that we only accept GeoJSONs of type
            "FeatureCollection" or "Feature" with geometries of
            type "Polygon" or "MultiPolygon".
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.choropleth.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        locationmode
            Determines the set of locations used to match entries
            in `locations` to regions on the map. Values "ISO-3",
            "USA-states", *country names* correspond to features on
            the base map and value "geojson-id" corresponds to
            features from a custom GeoJSON linked to the `geojson`
            attribute.
        locations
            Sets the coordinates via location IDs or names. See
            `locationmode` for more info.
        locationssrc
            Sets the source reference on Chart Studio Cloud for
            locations .
        marker
            :class:`plotly.graph_objects.choropleth.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        selected
            :class:`plotly.graph_objects.choropleth.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.choropleth.Stream`
            instance or dict with compatible properties
        text
            Sets the text elements associated with each location.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.choropleth.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        z
            Sets the color values.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Choropleth

        new_trace = Choropleth(
            autocolorscale=autocolorscale,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            featureidkey=featureidkey,
            geo=geo,
            geojson=geojson,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            locationmode=locationmode,
            locations=locations,
            locationssrc=locationssrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            reversescale=reversescale,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_choroplethmapbox(
        self,
        autocolorscale=None,
        below=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        featureidkey=None,
        geojson=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        locations=None,
        locationssrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        reversescale=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showscale=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Choroplethmapbox trace
        
        GeoJSON features to be filled are set in `geojson` The data
        that describes the choropleth value-to-color mapping is set in
        `locations` and `z`.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        below
            Determines if the choropleth polygons will be inserted
            before the layer with the specified ID. By default,
            choroplethmapbox traces are placed above the water
            layers. If set to '', the layer will be inserted above
            every existing layer.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.choroplethmapbox.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        featureidkey
            Sets the key in GeoJSON features which is used as id to
            match the items included in the `locations` array.
            Support nested property, for example "properties.name".
        geojson
            Sets the GeoJSON data associated with this trace. It
            can be set as a valid GeoJSON object or as a URL
            string. Note that we only accept GeoJSONs of type
            "FeatureCollection" or "Feature" with geometries of
            type "Polygon" or "MultiPolygon".
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.choroplethmapbox.Hoverlabe
            l` instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variable `properties` Anything contained
            in tag `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        locations
            Sets which features found in "geojson" to plot using
            their feature `id` field.
        locationssrc
            Sets the source reference on Chart Studio Cloud for
            locations .
        marker
            :class:`plotly.graph_objects.choroplethmapbox.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        selected
            :class:`plotly.graph_objects.choroplethmapbox.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.choroplethmapbox.Stream`
            instance or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a mapbox subplot. If "mapbox" (the default value),
            the data refer to `layout.mapbox`. If "mapbox2", the
            data refer to `layout.mapbox2`, and so on.
        text
            Sets the text elements associated with each location.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.choroplethmapbox.Unselecte
            d` instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        z
            Sets the color values.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Choroplethmapbox

        new_trace = Choroplethmapbox(
            autocolorscale=autocolorscale,
            below=below,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            featureidkey=featureidkey,
            geojson=geojson,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            locations=locations,
            locationssrc=locationssrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            reversescale=reversescale,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_cone(
        self,
        anchor=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        sizemode=None,
        sizeref=None,
        stream=None,
        text=None,
        textsrc=None,
        u=None,
        uid=None,
        uirevision=None,
        usrc=None,
        v=None,
        visible=None,
        vsrc=None,
        w=None,
        wsrc=None,
        x=None,
        xsrc=None,
        y=None,
        ysrc=None,
        z=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Cone trace
        
        Use cone traces to visualize vector fields.  Specify a vector
        field using 6 1D arrays, 3 position arrays `x`, `y` and `z` and
        3 vector component arrays `u`, `v`, `w`. The cones are drawn
        exactly at the positions given by `x`, `y` and `z`.

        Parameters
        ----------
        anchor
            Sets the cones' anchor with respect to their x/y/z
            positions. Note that "cm" denote the cone's center of
            mass which corresponds to 1/4 from the tail to tip.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here u/v/w norm) or the
            bounds set in `cmin` and `cmax`  Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as u/v/w norm. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmax`
            must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.cone.ColorBar` instance or
            dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.cone.Hoverlabel` instance
            or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variable `norm` Anything contained in
            tag `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lighting
            :class:`plotly.graph_objects.cone.Lighting` instance or
            dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.cone.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        sizemode
            Determines whether `sizeref` is set as a "scaled" (i.e
            unitless) scalar (normalized by the max u/v/w norm in
            the vector field) or as "absolute" value (in the same
            units as the vector field).
        sizeref
            Adjusts the cone size scaling. The size of the cones is
            determined by their u/v/w norm multiplied a factor and
            `sizeref`. This factor (computed internally)
            corresponds to the minimum "time" to travel across two
            successive x/y/z positions at the average velocity of
            those two successive positions. All cones in a given
            trace use the same factor. With `sizemode` set to
            "scaled", `sizeref` is unitless, its default value is
            0.5 With `sizemode` set to "absolute", `sizeref` has
            the same units as the u/v/w vector field, its the
            default value is half the sample's maximum vector norm.
        stream
            :class:`plotly.graph_objects.cone.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with the cones. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        u
            Sets the x components of the vector field.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        usrc
            Sets the source reference on Chart Studio Cloud for  u
            .
        v
            Sets the y components of the vector field.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        vsrc
            Sets the source reference on Chart Studio Cloud for  v
            .
        w
            Sets the z components of the vector field.
        wsrc
            Sets the source reference on Chart Studio Cloud for  w
            .
        x
            Sets the x coordinates of the vector field and of the
            displayed cones.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates of the vector field and of the
            displayed cones.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the z coordinates of the vector field and of the
            displayed cones.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Cone

        new_trace = Cone(
            anchor=anchor,
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            sizemode=sizemode,
            sizeref=sizeref,
            stream=stream,
            text=text,
            textsrc=textsrc,
            u=u,
            uid=uid,
            uirevision=uirevision,
            usrc=usrc,
            v=v,
            visible=visible,
            vsrc=vsrc,
            w=w,
            wsrc=wsrc,
            x=x,
            xsrc=xsrc,
            y=y,
            ysrc=ysrc,
            z=z,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_contour(
        self,
        autocolorscale=None,
        autocontour=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoverongaps=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Contour trace
        
        The data from which contour lines are computed is set in `z`.
        Data in `z` must be a 2D list of numbers. Say that `z` has N
        rows and M columns, then by default, these N rows correspond to
        N y coordinates (set in `y` or auto-generated) and the M
        columns correspond to M x coordinates (set in `x` or auto-
        generated). By setting `transpose` to True, the above behavior
        is flipped.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        autocontour
            Determines whether or not the contour level attributes
            are picked by an algorithm. If True, the number of
            contour levels can be set in `ncontours`. If False, set
            the contour level attributes in `contours`.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.contour.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data are filled in. It is defaulted
            to true if `z` is a one dimensional array otherwise it
            is defaulted to false.
        contours
            :class:`plotly.graph_objects.contour.Contours` instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        fillcolor
            Sets the fill color if `contours.type` is "constraint".
            Defaults to a half-transparent variant of the line
            color, marker color, or marker line color, whichever is
            available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.contour.Hoverlabel`
            instance or dict with compatible properties
        hoverongaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data have hover labels associated
            with them.
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.contour.Line` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        ncontours
            Sets the maximum number of contour levels. The actual
            number of contours will be chosen automatically to be
            less than or equal to the value of `ncontours`. Has an
            effect only if `autocontour` is True or if
            `contours.size` is missing.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.contour.Stream` instance
            or dict with compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        transpose
            Transposes the z data.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        xtype
            If "array", the heatmap's x coordinates are given by
            "x" (the default behavior when `x` is provided). If
            "scaled", the heatmap's x coordinates are given by "x0"
            and "dx" (the default behavior when `x` is not
            provided).
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        ytype
            If "array", the heatmap's y coordinates are given by
            "y" (the default behavior when `y` is provided) If
            "scaled", the heatmap's y coordinates are given by "y0"
            and "dy" (the default behavior when `y` is not
            provided)
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Contour

        new_trace = Contour(
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoverongaps=hoverongaps,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            xtype=xtype,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            ytype=ytype,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_contourcarpet(
        self,
        a=None,
        a0=None,
        asrc=None,
        atype=None,
        autocolorscale=None,
        autocontour=None,
        b=None,
        b0=None,
        bsrc=None,
        btype=None,
        carpet=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        fillcolor=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        xaxis=None,
        yaxis=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Contourcarpet trace
        
        Plots contours on either the first carpet axis or the carpet
        axis with a matching `carpet` attribute. Data `z` is
        interpreted as matching that of the corresponding carpet axis.

        Parameters
        ----------
        a
            Sets the x coordinates.
        a0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        asrc
            Sets the source reference on Chart Studio Cloud for  a
            .
        atype
            If "array", the heatmap's x coordinates are given by
            "x" (the default behavior when `x` is provided). If
            "scaled", the heatmap's x coordinates are given by "x0"
            and "dx" (the default behavior when `x` is not
            provided).
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        autocontour
            Determines whether or not the contour level attributes
            are picked by an algorithm. If True, the number of
            contour levels can be set in `ncontours`. If False, set
            the contour level attributes in `contours`.
        b
            Sets the y coordinates.
        b0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        bsrc
            Sets the source reference on Chart Studio Cloud for  b
            .
        btype
            If "array", the heatmap's y coordinates are given by
            "y" (the default behavior when `y` is provided) If
            "scaled", the heatmap's y coordinates are given by "y0"
            and "dy" (the default behavior when `y` is not
            provided)
        carpet
            The `carpet` of the carpet axes on which this contour
            trace lies
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.contourcarpet.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contours
            :class:`plotly.graph_objects.contourcarpet.Contours`
            instance or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        da
            Sets the x coordinate step. See `x0` for more info.
        db
            Sets the y coordinate step. See `y0` for more info.
        fillcolor
            Sets the fill color if `contours.type` is "constraint".
            Defaults to a half-transparent variant of the line
            color, marker color, or marker line color, whichever is
            available.
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.contourcarpet.Line`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        ncontours
            Sets the maximum number of contour levels. The actual
            number of contours will be chosen automatically to be
            less than or equal to the value of `ncontours`. Has an
            effect only if `autocontour` is True or if
            `contours.size` is missing.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.contourcarpet.Stream`
            instance or dict with compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        transpose
            Transposes the z data.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Contourcarpet

        new_trace = Contourcarpet(
            a=a,
            a0=a0,
            asrc=asrc,
            atype=atype,
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            b=b,
            b0=b0,
            bsrc=bsrc,
            btype=btype,
            carpet=carpet,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            da=da,
            db=db,
            fillcolor=fillcolor,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            xaxis=xaxis,
            yaxis=yaxis,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_densitymapbox(
        self,
        autocolorscale=None,
        below=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legendgroup=None,
        lon=None,
        lonsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        radius=None,
        radiussrc=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Densitymapbox trace
        
        Draws a bivariate kernel density estimation with a Gaussian
        kernel from `lon` and `lat` coordinates and optional `z` values
        using a colorscale.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        below
            Determines if the densitymapbox trace will be inserted
            before the layer with the specified ID. By default,
            densitymapbox traces are placed below the first layer
            of type symbol If set to '', the layer will be inserted
            above every existing layer.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.densitymapbox.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.densitymapbox.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (lon,lat)
            pair If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (lon,lat)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        lat
            Sets the latitude coordinates (in degrees North).
        latsrc
            Sets the source reference on Chart Studio Cloud for
            lat .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lon
            Sets the longitude coordinates (in degrees East).
        lonsrc
            Sets the source reference on Chart Studio Cloud for
            lon .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        radius
            Sets the radius of influence of one `lon` / `lat` point
            in pixels. Increasing the value makes the densitymapbox
            trace smoother, but less detailed.
        radiussrc
            Sets the source reference on Chart Studio Cloud for
            radius .
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.densitymapbox.Stream`
            instance or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a mapbox subplot. If "mapbox" (the default value),
            the data refer to `layout.mapbox`. If "mapbox2", the
            data refer to `layout.mapbox2`, and so on.
        text
            Sets text elements associated with each (lon,lat) pair
            If a single string, the same string appears over all
            the data points. If an array of string, the items are
            mapped in order to the this trace's (lon,lat)
            coordinates. If trace `hoverinfo` contains a "text"
            flag and "hovertext" is not set, these elements will be
            seen in the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        z
            Sets the points' weight. For example, a value of 10
            would be equivalent to having 10 points of weight 1 in
            the same spot
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Densitymapbox

        new_trace = Densitymapbox(
            autocolorscale=autocolorscale,
            below=below,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legendgroup=legendgroup,
            lon=lon,
            lonsrc=lonsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            radius=radius,
            radiussrc=radiussrc,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_funnel(
        self,
        alignmentgroup=None,
        cliponaxis=None,
        connector=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Funnel trace
        
        Visualize stages in a process using length-encoded bars. This
        trace can be used to show data in either a part-to-whole
        representation wherein each item appears in a single stage, or
        in a "drop-off" representation wherein each item appears in
        each stage it traversed. See also the "funnelarea" trace type
        for a different approach to visualizing funnel data.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        connector
            :class:`plotly.graph_objects.funnel.Connector` instance
            or dict with compatible properties
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.funnel.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `percentInitial`,
            `percentPrevious` and `percentTotal`. Anything
            contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        insidetextanchor
            Determines if texts are kept at center or start/end
            points in `textposition` "inside" mode.
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.funnel.Marker` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the funnels. With "v" ("h"),
            the value of the each bar spans along the vertical
            (horizontal). By default funnels are tend to be
            oriented horizontally; unless only "y" array is
            presented or orientation is set to "v". Also regarding
            graphs including only 'horizontal' funnels, "autorange"
            on the "y-axis" are set to "reversed".
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.funnel.Stream` instance or
            dict with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textangle
            Sets the angle of the tick labels with respect to the
            bar. For example, a `tickangle` of -90 draws the tick
            labels vertically. With "auto" the texts may
            automatically be rotated to fit with the maximum size
            in bars.
        textfont
            Sets the font used for `text`.
        textinfo
            Determines which trace information appear on the graph.
            In the case of having multiple funnels, percentages &
            totals are computed separately (per trace).
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed), unless
            there is another bar stacked on this one, then the text
            gets pushed inside. "auto" tries to position `text`
            inside the bar, but if the bar is too small and no bar
            is stacked on this one the text is moved outside.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables
            `percentInitial`, `percentPrevious`, `percentTotal`,
            `label` and `value`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Funnel

        new_trace = Funnel(
            alignmentgroup=alignmentgroup,
            cliponaxis=cliponaxis,
            connector=connector,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_funnelarea(
        self,
        aspectratio=None,
        baseratio=None,
        customdata=None,
        customdatasrc=None,
        dlabel=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        label0=None,
        labels=None,
        labelssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        scalegroup=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        title=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Funnelarea trace
        
        Visualize stages in a process using area-encoded trapezoids.
        This trace can be used to show data in a part-to-whole
        representation similar to a "pie" trace, wherein each item
        appears in a single stage. See also the "funnel" trace type for
        a different approach to visualizing funnel data.

        Parameters
        ----------
        aspectratio
            Sets the ratio between height and width
        baseratio
            Sets the ratio between bottom length and maximum top
            length.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dlabel
            Sets the label step. See `label0` for more info.
        domain
            :class:`plotly.graph_objects.funnelarea.Domain`
            instance or dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.funnelarea.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `label`, `color`, `value`,
            `text` and `percent`. Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        label0
            Alternate to `labels`. Builds a numeric set of labels.
            Use with `dlabel` where `label0` is the starting label
            and `dlabel` the step.
        labels
            Sets the sector labels. If `labels` entries are
            duplicated, we sum associated `values` or simply count
            occurrences if `values` is not provided. For other
            array attributes (including color) we use the first
            non-empty entry among all occurrences of the label.
        labelssrc
            Sets the source reference on Chart Studio Cloud for
            labels .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.funnelarea.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        scalegroup
            If there are multiple funnelareas that should be sized
            according to their totals, link them by providing a
            non-empty group id here shared by every trace in the
            same group.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.funnelarea.Stream`
            instance or dict with compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Specifies the location of the `textinfo`.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `label`,
            `color`, `value`, `text` and `percent`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        title
            :class:`plotly.graph_objects.funnelarea.Title` instance
            or dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        values
            Sets the values of the sectors. If omitted, we count
            occurrences of each label.
        valuessrc
            Sets the source reference on Chart Studio Cloud for
            values .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Funnelarea

        new_trace = Funnelarea(
            aspectratio=aspectratio,
            baseratio=baseratio,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dlabel=dlabel,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            label0=label0,
            labels=labels,
            labelssrc=labelssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            scalegroup=scalegroup,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            title=title,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_heatmap(
        self,
        autocolorscale=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoverongaps=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xgap=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ygap=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsmooth=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Heatmap trace
        
        The data that describes the heatmap value-to-color mapping is
        set in `z`. Data in `z` can either be a 2D list of values
        (ragged or not) or a 1D array of values. In the case where `z`
        is a 2D list, say that `z` has N rows and M columns. Then, by
        default, the resulting heatmap will have N partitions along the
        y axis and M partitions along the x axis. In other words, the
        i-th row/ j-th column cell in `z` is mapped to the i-th
        partition of the y axis (starting from the bottom of the plot)
        and the j-th partition of the x-axis (starting from the left of
        the plot). This behavior can be flipped by using `transpose`.
        Moreover, `x` (`y`) can be provided with M or M+1 (N or N+1)
        elements. If M (N), then the coordinates correspond to the
        center of the heatmap cells and the cells have equal width. If
        M+1 (N+1), then the coordinates correspond to the edges of the
        heatmap cells. In the case where `z` is a 1D list, the x and y
        coordinates must be provided in `x` and `y` respectively to
        form data triplets.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.heatmap.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data are filled in. It is defaulted
            to true if `z` is a one dimensional array and `zsmooth`
            is not false; otherwise it is defaulted to false.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.heatmap.Hoverlabel`
            instance or dict with compatible properties
        hoverongaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data have hover labels associated
            with them.
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.heatmap.Stream` instance
            or dict with compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        transpose
            Transposes the z data.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xgap
            Sets the horizontal gap (in pixels) between bricks.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        xtype
            If "array", the heatmap's x coordinates are given by
            "x" (the default behavior when `x` is provided). If
            "scaled", the heatmap's x coordinates are given by "x0"
            and "dx" (the default behavior when `x` is not
            provided).
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ygap
            Sets the vertical gap (in pixels) between bricks.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        ytype
            If "array", the heatmap's y coordinates are given by
            "y" (the default behavior when `y` is provided) If
            "scaled", the heatmap's y coordinates are given by "y0"
            and "dy" (the default behavior when `y` is not
            provided)
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsmooth
            Picks a smoothing algorithm use to smooth `z` data.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Heatmap

        new_trace = Heatmap(
            autocolorscale=autocolorscale,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoverongaps=hoverongaps,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xgap=xgap,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            xtype=xtype,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            ygap=ygap,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            ytype=ytype,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsmooth=zsmooth,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_heatmapgl(
        self,
        autocolorscale=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsmooth=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Heatmapgl trace
        
        WebGL version of the heatmap trace type.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.heatmapgl.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.heatmapgl.Hoverlabel`
            instance or dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.heatmapgl.Stream` instance
            or dict with compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        transpose
            Transposes the z data.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        xtype
            If "array", the heatmap's x coordinates are given by
            "x" (the default behavior when `x` is provided). If
            "scaled", the heatmap's x coordinates are given by "x0"
            and "dx" (the default behavior when `x` is not
            provided).
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        ytype
            If "array", the heatmap's y coordinates are given by
            "y" (the default behavior when `y` is provided) If
            "scaled", the heatmap's y coordinates are given by "y0"
            and "dy" (the default behavior when `y` is not
            provided)
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsmooth
            Picks a smoothing algorithm use to smooth `z` data.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Heatmapgl

        new_trace = Heatmapgl(
            autocolorscale=autocolorscale,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xsrc=xsrc,
            xtype=xtype,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ysrc=ysrc,
            ytype=ytype,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsmooth=zsmooth,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_histogram(
        self,
        alignmentgroup=None,
        autobinx=None,
        autobiny=None,
        bingroup=None,
        cumulative=None,
        customdata=None,
        customdatasrc=None,
        error_x=None,
        error_y=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        xaxis=None,
        xbins=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybins=None,
        ycalendar=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Histogram trace
        
        The sample data from which statistics are computed is set in
        `x` for vertically spanning histograms and in `y` for
        horizontally spanning histograms. Binning options are set
        `xbins` and `ybins` respectively if no aggregation data is
        provided.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        autobinx
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobinx` is not needed.
            However, we accept `autobinx: true` or `false` and will
            update `xbins` accordingly before deleting `autobinx`
            from the trace.
        autobiny
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobiny` is not needed.
            However, we accept `autobiny: true` or `false` and will
            update `ybins` accordingly before deleting `autobiny`
            from the trace.
        bingroup
            Set a group of histogram traces which will have
            compatible bin settings. Note that traces on the same
            subplot and with the same "orientation" under `barmode`
            "stack", "relative" and "group" are forced into the
            same bingroup, Using `bingroup`, traces under `barmode`
            "overlay" and on different axes (of the same axis type)
            can have compatible bin settings. Note that histogram
            and histogram2d* trace can share the same `bingroup`
        cumulative
            :class:`plotly.graph_objects.histogram.Cumulative`
            instance or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        error_x
            :class:`plotly.graph_objects.histogram.ErrorX` instance
            or dict with compatible properties
        error_y
            :class:`plotly.graph_objects.histogram.ErrorY` instance
            or dict with compatible properties
        histfunc
            Specifies the binning function used for this histogram
            trace. If "count", the histogram values are computed by
            counting the number of values lying inside each bin. If
            "sum", "avg", "min", "max", the histogram values are
            computed using the sum, the average, the minimum or the
            maximum of the values lying inside each bin
            respectively.
        histnorm
            Specifies the type of normalization used for this
            histogram trace. If "", the span of each bar
            corresponds to the number of occurrences (i.e. the
            number of data points lying inside the bins). If
            "percent" / "probability", the span of each bar
            corresponds to the percentage / fraction of occurrences
            with respect to the total number of sample points
            (here, the sum of all bin HEIGHTS equals 100% / 1). If
            "density", the span of each bar corresponds to the
            number of occurrences in a bin divided by the size of
            the bin interval (here, the sum of all bin AREAS equals
            the total number of sample points). If *probability
            density*, the area of each bar corresponds to the
            probability that an event will fall into the
            corresponding bin (here, the sum of all bin AREAS
            equals 1).
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.histogram.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variable `binNumber` Anything contained
            in tag `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.histogram.Marker` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        nbinsx
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `xbins.size` is provided.
        nbinsy
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `ybins.size` is provided.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        selected
            :class:`plotly.graph_objects.histogram.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.histogram.Stream` instance
            or dict with compatible properties
        text
            Sets hover text elements associated with each bar. If a
            single string, the same string appears over all bars.
            If an array of string, the items are mapped in order to
            the this trace's coordinates.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.histogram.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the sample data to be binned on the x axis.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbins
            :class:`plotly.graph_objects.histogram.XBins` instance
            or dict with compatible properties
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the sample data to be binned on the y axis.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybins
            :class:`plotly.graph_objects.histogram.YBins` instance
            or dict with compatible properties
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Histogram

        new_trace = Histogram(
            alignmentgroup=alignmentgroup,
            autobinx=autobinx,
            autobiny=autobiny,
            bingroup=bingroup,
            cumulative=cumulative,
            customdata=customdata,
            customdatasrc=customdatasrc,
            error_x=error_x,
            error_y=error_y,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbins=xbins,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybins=ybins,
            ycalendar=ycalendar,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_histogram2d(
        self,
        autobinx=None,
        autobiny=None,
        autocolorscale=None,
        bingroup=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbingroup=None,
        xbins=None,
        xcalendar=None,
        xgap=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybingroup=None,
        ybins=None,
        ycalendar=None,
        ygap=None,
        ysrc=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsmooth=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Histogram2d trace
        
        The sample data from which statistics are computed is set in
        `x` and `y` (where `x` and `y` represent marginal
        distributions, binning is set in `xbins` and `ybins` in this
        case) or `z` (where `z` represent the 2D distribution and
        binning set, binning is set by `x` and `y` in this case). The
        resulting distribution is visualized as a heatmap.

        Parameters
        ----------
        autobinx
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobinx` is not needed.
            However, we accept `autobinx: true` or `false` and will
            update `xbins` accordingly before deleting `autobinx`
            from the trace.
        autobiny
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobiny` is not needed.
            However, we accept `autobiny: true` or `false` and will
            update `ybins` accordingly before deleting `autobiny`
            from the trace.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        bingroup
            Set the `xbingroup` and `ybingroup` default prefix For
            example, setting a `bingroup` of 1 on two histogram2d
            traces will make them their x-bins and y-bins match
            separately.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.histogram2d.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        histfunc
            Specifies the binning function used for this histogram
            trace. If "count", the histogram values are computed by
            counting the number of values lying inside each bin. If
            "sum", "avg", "min", "max", the histogram values are
            computed using the sum, the average, the minimum or the
            maximum of the values lying inside each bin
            respectively.
        histnorm
            Specifies the type of normalization used for this
            histogram trace. If "", the span of each bar
            corresponds to the number of occurrences (i.e. the
            number of data points lying inside the bins). If
            "percent" / "probability", the span of each bar
            corresponds to the percentage / fraction of occurrences
            with respect to the total number of sample points
            (here, the sum of all bin HEIGHTS equals 100% / 1). If
            "density", the span of each bar corresponds to the
            number of occurrences in a bin divided by the size of
            the bin interval (here, the sum of all bin AREAS equals
            the total number of sample points). If *probability
            density*, the area of each bar corresponds to the
            probability that an event will fall into the
            corresponding bin (here, the sum of all bin AREAS
            equals 1).
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.histogram2d.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variable `z` Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.histogram2d.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        nbinsx
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `xbins.size` is provided.
        nbinsy
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `ybins.size` is provided.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.histogram2d.Stream`
            instance or dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the sample data to be binned on the x axis.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbingroup
            Set a group of histogram traces which will have
            compatible x-bin settings. Using `xbingroup`,
            histogram2d and histogram2dcontour traces  (on axes of
            the same axis type) can have compatible x-bin settings.
            Note that the same `xbingroup` value can be used to set
            (1D) histogram `bingroup`
        xbins
            :class:`plotly.graph_objects.histogram2d.XBins`
            instance or dict with compatible properties
        xcalendar
            Sets the calendar system to use with `x` date data.
        xgap
            Sets the horizontal gap (in pixels) between bricks.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the sample data to be binned on the y axis.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybingroup
            Set a group of histogram traces which will have
            compatible y-bin settings. Using `ybingroup`,
            histogram2d and histogram2dcontour traces  (on axes of
            the same axis type) can have compatible y-bin settings.
            Note that the same `ybingroup` value can be used to set
            (1D) histogram `bingroup`
        ybins
            :class:`plotly.graph_objects.histogram2d.YBins`
            instance or dict with compatible properties
        ycalendar
            Sets the calendar system to use with `y` date data.
        ygap
            Sets the vertical gap (in pixels) between bricks.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the aggregation data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsmooth
            Picks a smoothing algorithm use to smooth `z` data.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Histogram2d

        new_trace = Histogram2d(
            autobinx=autobinx,
            autobiny=autobiny,
            autocolorscale=autocolorscale,
            bingroup=bingroup,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbingroup=xbingroup,
            xbins=xbins,
            xcalendar=xcalendar,
            xgap=xgap,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybingroup=ybingroup,
            ybins=ybins,
            ycalendar=ycalendar,
            ygap=ygap,
            ysrc=ysrc,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsmooth=zsmooth,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_histogram2dcontour(
        self,
        autobinx=None,
        autobiny=None,
        autocolorscale=None,
        autocontour=None,
        bingroup=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbingroup=None,
        xbins=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybingroup=None,
        ybins=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Histogram2dContour trace
        
        The sample data from which statistics are computed is set in
        `x` and `y` (where `x` and `y` represent marginal
        distributions, binning is set in `xbins` and `ybins` in this
        case) or `z` (where `z` represent the 2D distribution and
        binning set, binning is set by `x` and `y` in this case). The
        resulting distribution is visualized as a contour plot.

        Parameters
        ----------
        autobinx
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobinx` is not needed.
            However, we accept `autobinx: true` or `false` and will
            update `xbins` accordingly before deleting `autobinx`
            from the trace.
        autobiny
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobiny` is not needed.
            However, we accept `autobiny: true` or `false` and will
            update `ybins` accordingly before deleting `autobiny`
            from the trace.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        autocontour
            Determines whether or not the contour level attributes
            are picked by an algorithm. If True, the number of
            contour levels can be set in `ncontours`. If False, set
            the contour level attributes in `contours`.
        bingroup
            Set the `xbingroup` and `ybingroup` default prefix For
            example, setting a `bingroup` of 1 on two histogram2d
            traces will make them their x-bins and y-bins match
            separately.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.histogram2dcontour.ColorBa
            r` instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contours
            :class:`plotly.graph_objects.histogram2dcontour.Contour
            s` instance or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        histfunc
            Specifies the binning function used for this histogram
            trace. If "count", the histogram values are computed by
            counting the number of values lying inside each bin. If
            "sum", "avg", "min", "max", the histogram values are
            computed using the sum, the average, the minimum or the
            maximum of the values lying inside each bin
            respectively.
        histnorm
            Specifies the type of normalization used for this
            histogram trace. If "", the span of each bar
            corresponds to the number of occurrences (i.e. the
            number of data points lying inside the bins). If
            "percent" / "probability", the span of each bar
            corresponds to the percentage / fraction of occurrences
            with respect to the total number of sample points
            (here, the sum of all bin HEIGHTS equals 100% / 1). If
            "density", the span of each bar corresponds to the
            number of occurrences in a bin divided by the size of
            the bin interval (here, the sum of all bin AREAS equals
            the total number of sample points). If *probability
            density*, the area of each bar corresponds to the
            probability that an event will fall into the
            corresponding bin (here, the sum of all bin AREAS
            equals 1).
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.histogram2dcontour.Hoverla
            bel` instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variable `z` Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.histogram2dcontour.Line`
            instance or dict with compatible properties
        marker
            :class:`plotly.graph_objects.histogram2dcontour.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        nbinsx
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `xbins.size` is provided.
        nbinsy
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `ybins.size` is provided.
        ncontours
            Sets the maximum number of contour levels. The actual
            number of contours will be chosen automatically to be
            less than or equal to the value of `ncontours`. Has an
            effect only if `autocontour` is True or if
            `contours.size` is missing.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.histogram2dcontour.Stream`
            instance or dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the sample data to be binned on the x axis.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbingroup
            Set a group of histogram traces which will have
            compatible x-bin settings. Using `xbingroup`,
            histogram2d and histogram2dcontour traces  (on axes of
            the same axis type) can have compatible x-bin settings.
            Note that the same `xbingroup` value can be used to set
            (1D) histogram `bingroup`
        xbins
            :class:`plotly.graph_objects.histogram2dcontour.XBins`
            instance or dict with compatible properties
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the sample data to be binned on the y axis.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybingroup
            Set a group of histogram traces which will have
            compatible y-bin settings. Using `ybingroup`,
            histogram2d and histogram2dcontour traces  (on axes of
            the same axis type) can have compatible y-bin settings.
            Note that the same `ybingroup` value can be used to set
            (1D) histogram `bingroup`
        ybins
            :class:`plotly.graph_objects.histogram2dcontour.YBins`
            instance or dict with compatible properties
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the aggregation data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmid
            Sets the mid-point of the color domain by scaling
            `zmin` and/or `zmax` to be equidistant to this point.
            Value should have the same units as in `z`. Has no
            effect when `zauto` is `false`.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Histogram2dContour

        new_trace = Histogram2dContour(
            autobinx=autobinx,
            autobiny=autobiny,
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            bingroup=bingroup,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbingroup=xbingroup,
            xbins=xbins,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybingroup=ybingroup,
            ybins=ybins,
            ycalendar=ycalendar,
            ysrc=ysrc,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_image(
        self,
        colormodel=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        source=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x0=None,
        xaxis=None,
        y0=None,
        yaxis=None,
        z=None,
        zmax=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Image trace
        
        Display an image, i.e. data on a 2D regular raster. By default,
        when an image is displayed in a subplot, its y axis will be
        reversed (ie. `autorange: 'reversed'`), constrained to the
        domain (ie. `constrain: 'domain'`) and it will have the same
        scale as its x axis (ie. `scaleanchor: 'x,`) in order for
        pixels to be rendered as squares.

        Parameters
        ----------
        colormodel
            Color model used to map the numerical color components
            described in `z` into colors. If `source` is specified,
            this attribute will be set to `rgba256` otherwise it
            defaults to `rgb`.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Set the pixel's horizontal size.
        dy
            Set the pixel's vertical size
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.image.Hoverlabel` instance
            or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `z`, `color` and `colormodel`.
            Anything contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        source
            Specifies the data URI of the image to be visualized.
            The URI consists of "data:image/[<media
            subtype>][;base64],<data>"
        stream
            :class:`plotly.graph_objects.image.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x0
            Set the image's x position.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        y0
            Set the image's y position.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        z
            A 2-dimensional array in which each element is an array
            of 3 or 4 numbers representing a color.
        zmax
            Array defining the higher bound for each color
            component. Note that the default value will depend on
            the colormodel. For the `rgb` colormodel, it is [255,
            255, 255]. For the `rgba` colormodel, it is [255, 255,
            255, 1]. For the `rgba256` colormodel, it is [255, 255,
            255, 255]. For the `hsl` colormodel, it is [360, 100,
            100]. For the `hsla` colormodel, it is [360, 100, 100,
            1].
        zmin
            Array defining the lower bound for each color
            component. Note that the default value will depend on
            the colormodel. For the `rgb` colormodel, it is [0, 0,
            0]. For the `rgba` colormodel, it is [0, 0, 0, 0]. For
            the `rgba256` colormodel, it is [0, 0, 0, 0]. For the
            `hsl` colormodel, it is [0, 0, 0]. For the `hsla`
            colormodel, it is [0, 0, 0, 0].
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Image

        new_trace = Image(
            colormodel=colormodel,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            source=source,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x0=x0,
            xaxis=xaxis,
            y0=y0,
            yaxis=yaxis,
            z=z,
            zmax=zmax,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_indicator(
        self,
        align=None,
        customdata=None,
        customdatasrc=None,
        delta=None,
        domain=None,
        gauge=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        number=None,
        stream=None,
        title=None,
        uid=None,
        uirevision=None,
        value=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Indicator trace
        
        An indicator is used to visualize a single `value` along with
        some contextual information such as `steps` or a `threshold`,
        using a combination of three visual elements: a number, a
        delta, and/or a gauge. Deltas are taken with respect to a
        `reference`. Gauges can be either angular or bullet (aka
        linear) gauges.

        Parameters
        ----------
        align
            Sets the horizontal alignment of the `text` within the
            box. Note that this attribute has no effect if an
            angular gauge is displayed: in this case, it is always
            centered
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        delta
            :class:`plotly.graph_objects.indicator.Delta` instance
            or dict with compatible properties
        domain
            :class:`plotly.graph_objects.indicator.Domain` instance
            or dict with compatible properties
        gauge
            The gauge of the Indicator plot.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines how the value is displayed on the graph.
            `number` displays the value numerically in text.
            `delta` displays the difference to a reference value in
            text. Finally, `gauge` displays the value graphically
            on an axis.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        number
            :class:`plotly.graph_objects.indicator.Number` instance
            or dict with compatible properties
        stream
            :class:`plotly.graph_objects.indicator.Stream` instance
            or dict with compatible properties
        title
            :class:`plotly.graph_objects.indicator.Title` instance
            or dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        value
            Sets the number to be displayed.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Indicator

        new_trace = Indicator(
            align=align,
            customdata=customdata,
            customdatasrc=customdatasrc,
            delta=delta,
            domain=domain,
            gauge=gauge,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            number=number,
            stream=stream,
            title=title,
            uid=uid,
            uirevision=uirevision,
            value=value,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_isosurface(
        self,
        autocolorscale=None,
        caps=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        isomax=None,
        isomin=None,
        legendgroup=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        slices=None,
        spaceframe=None,
        stream=None,
        surface=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        value=None,
        valuesrc=None,
        visible=None,
        x=None,
        xsrc=None,
        y=None,
        ysrc=None,
        z=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Isosurface trace
        
        Draws isosurfaces between iso-min and iso-max values with
        coordinates given by four 1-dimensional arrays containing the
        `value`, `x`, `y` and `z` of every vertex of a uniform or non-
        uniform 3-D grid. Horizontal or vertical slices, caps as well
        as spaceframe between iso-min and iso-max values could also be
        drawn using this trace.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        caps
            :class:`plotly.graph_objects.isosurface.Caps` instance
            or dict with compatible properties
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `value`) or the
            bounds set in `cmin` and `cmax`  Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `value` and if set, `cmin` must
            be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `value`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `value` and if set, `cmax` must
            be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.isosurface.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contour
            :class:`plotly.graph_objects.isosurface.Contour`
            instance or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.isosurface.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        isomax
            Sets the maximum boundary for iso-surface plot.
        isomin
            Sets the minimum boundary for iso-surface plot.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lighting
            :class:`plotly.graph_objects.isosurface.Lighting`
            instance or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.isosurface.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        slices
            :class:`plotly.graph_objects.isosurface.Slices`
            instance or dict with compatible properties
        spaceframe
            :class:`plotly.graph_objects.isosurface.Spaceframe`
            instance or dict with compatible properties
        stream
            :class:`plotly.graph_objects.isosurface.Stream`
            instance or dict with compatible properties
        surface
            :class:`plotly.graph_objects.isosurface.Surface`
            instance or dict with compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        value
            Sets the 4th dimension (value) of the vertices.
        valuesrc
            Sets the source reference on Chart Studio Cloud for
            value .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices on X axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the Y coordinates of the vertices on Y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the Z coordinates of the vertices on Z axis.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Isosurface

        new_trace = Isosurface(
            autocolorscale=autocolorscale,
            caps=caps,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            isomax=isomax,
            isomin=isomin,
            legendgroup=legendgroup,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            slices=slices,
            spaceframe=spaceframe,
            stream=stream,
            surface=surface,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            value=value,
            valuesrc=valuesrc,
            visible=visible,
            x=x,
            xsrc=xsrc,
            y=y,
            ysrc=ysrc,
            z=z,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_mesh3d(
        self,
        alphahull=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        color=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        delaunayaxis=None,
        facecolor=None,
        facecolorsrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        i=None,
        ids=None,
        idssrc=None,
        intensity=None,
        intensitymode=None,
        intensitysrc=None,
        isrc=None,
        j=None,
        jsrc=None,
        k=None,
        ksrc=None,
        legendgroup=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        vertexcolor=None,
        vertexcolorsrc=None,
        visible=None,
        x=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Mesh3d trace
        
        Draws sets of triangles with coordinates given by three
        1-dimensional arrays in `x`, `y`, `z` and (1) a sets of `i`,
        `j`, `k` indices (2) Delaunay triangulation or (3) the Alpha-
        shape algorithm or (4) the Convex-hull algorithm

        Parameters
        ----------
        alphahull
            Determines how the mesh surface triangles are derived
            from the set of vertices (points) represented by the
            `x`, `y` and `z` arrays, if the `i`, `j`, `k` arrays
            are not supplied. For general use of `mesh3d` it is
            preferred that `i`, `j`, `k` are supplied. If "-1",
            Delaunay triangulation is used, which is mainly
            suitable if the mesh is a single, more or less layer
            surface that is perpendicular to `delaunayaxis`. In
            case the `delaunayaxis` intersects the mesh surface at
            more than one point it will result triangles that are
            very long in the dimension of `delaunayaxis`. If ">0",
            the alpha-shape algorithm is used. In this case, the
            positive `alphahull` value signals the use of the
            alpha-shape algorithm, _and_ its value acts as the
            parameter for the mesh fitting. If 0,  the convex-hull
            algorithm is used. It is suitable for convex bodies or
            if the intention is to enclose the `x`, `y` and `z`
            point set into a convex hull.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `intensity`) or
            the bounds set in `cmin` and `cmax`  Defaults to
            `false` when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `intensity` and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `intensity`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `intensity` and if set, `cmax`
            must be set as well.
        color
            Sets the color of the whole mesh
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.mesh3d.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contour
            :class:`plotly.graph_objects.mesh3d.Contour` instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        delaunayaxis
            Sets the Delaunay axis, which is the axis that is
            perpendicular to the surface of the Delaunay
            triangulation. It has an effect if `i`, `j`, `k` are
            not provided and `alphahull` is set to indicate
            Delaunay triangulation.
        facecolor
            Sets the color of each face Overrides "color" and
            "vertexcolor".
        facecolorsrc
            Sets the source reference on Chart Studio Cloud for
            facecolor .
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.mesh3d.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        i
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "first" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `i[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `i` represents a point in space, which
            is the first vertex of a triangle.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        intensity
            Sets the intensity values for vertices or cells as
            defined by `intensitymode`. It can be used for plotting
            fields on meshes.
        intensitymode
            Determines the source of `intensity` values.
        intensitysrc
            Sets the source reference on Chart Studio Cloud for
            intensity .
        isrc
            Sets the source reference on Chart Studio Cloud for  i
            .
        j
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "second" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}`  together represent face m (triangle m) in
            the mesh, where `j[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `j` represents a point in space, which
            is the second vertex of a triangle.
        jsrc
            Sets the source reference on Chart Studio Cloud for  j
            .
        k
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "third" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `k[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `k` represents a point in space, which
            is the third vertex of a triangle.
        ksrc
            Sets the source reference on Chart Studio Cloud for  k
            .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lighting
            :class:`plotly.graph_objects.mesh3d.Lighting` instance
            or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.mesh3d.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.mesh3d.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        vertexcolor
            Sets the color of each vertex Overrides "color". While
            Red, green and blue colors are in the range of 0 and
            255; in the case of having vertex color data in RGBA
            format, the alpha color should be normalized to be
            between 0 and 1.
        vertexcolorsrc
            Sets the source reference on Chart Studio Cloud for
            vertexcolor .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the Y coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the Z coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Mesh3d

        new_trace = Mesh3d(
            alphahull=alphahull,
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            color=color,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            delaunayaxis=delaunayaxis,
            facecolor=facecolor,
            facecolorsrc=facecolorsrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            i=i,
            ids=ids,
            idssrc=idssrc,
            intensity=intensity,
            intensitymode=intensitymode,
            intensitysrc=intensitysrc,
            isrc=isrc,
            j=j,
            jsrc=jsrc,
            k=k,
            ksrc=ksrc,
            legendgroup=legendgroup,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            vertexcolor=vertexcolor,
            vertexcolorsrc=vertexcolorsrc,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_ohlc(
        self,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legendgroup=None,
        line=None,
        low=None,
        lowsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        tickwidth=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        yaxis=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Ohlc trace
        
        The ohlc (short for Open-High-Low-Close) is a style of
        financial chart describing open, high, low and close for a
        given `x` coordinate (most likely time). The tip of the lines
        represent the `low` and `high` values and the horizontal
        segments represent the `open` and `close` values. Sample points
        where the close value is higher (lower) then the open value are
        called increasing (decreasing). By default, increasing items
        are drawn in green whereas decreasing are drawn in red.

        Parameters
        ----------
        close
            Sets the close values.
        closesrc
            Sets the source reference on Chart Studio Cloud for
            close .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        decreasing
            :class:`plotly.graph_objects.ohlc.Decreasing` instance
            or dict with compatible properties
        high
            Sets the high values.
        highsrc
            Sets the source reference on Chart Studio Cloud for
            high .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.ohlc.Hoverlabel` instance
            or dict with compatible properties
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        increasing
            :class:`plotly.graph_objects.ohlc.Increasing` instance
            or dict with compatible properties
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.ohlc.Line` instance or
            dict with compatible properties
        low
            Sets the low values.
        lowsrc
            Sets the source reference on Chart Studio Cloud for
            low .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        open
            Sets the open values.
        opensrc
            Sets the source reference on Chart Studio Cloud for
            open .
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.ohlc.Stream` instance or
            dict with compatible properties
        text
            Sets hover text elements associated with each sample
            point. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to this trace's sample points.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        tickwidth
            Sets the width of the open/close tick marks relative to
            the "x" minimal interval.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates. If absent, linear coordinate
            will be generated.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Ohlc

        new_trace = Ohlc(
            close=close,
            closesrc=closesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            high=high,
            highsrc=highsrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            legendgroup=legendgroup,
            line=line,
            low=low,
            lowsrc=lowsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            open=open,
            opensrc=opensrc,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            tickwidth=tickwidth,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            yaxis=yaxis,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_parcats(
        self,
        arrangement=None,
        bundlecolors=None,
        counts=None,
        countssrc=None,
        dimensions=None,
        dimensiondefaults=None,
        domain=None,
        hoverinfo=None,
        hoveron=None,
        hovertemplate=None,
        labelfont=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        sortpaths=None,
        stream=None,
        tickfont=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Parcats trace
        
        Parallel categories diagram for multidimensional categorical
        data.

        Parameters
        ----------
        arrangement
            Sets the drag interaction mode for categories and
            dimensions. If `perpendicular`, the categories can only
            move along a line perpendicular to the paths. If
            `freeform`, the categories can freely move on the
            plane. If `fixed`, the categories and dimensions are
            stationary.
        bundlecolors
            Sort paths so that like colors are bundled together
            within each category.
        counts
            The number of observations represented by each state.
            Defaults to 1 so that each state represents one
            observation
        countssrc
            Sets the source reference on Chart Studio Cloud for
            counts .
        dimensions
            The dimensions (variables) of the parallel categories
            diagram.
        dimensiondefaults
            When used in a template (as
            layout.template.data.parcats.dimensiondefaults), sets
            the default property values to use for elements of
            parcats.dimensions
        domain
            :class:`plotly.graph_objects.parcats.Domain` instance
            or dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoveron
            Sets the hover interaction mode for the parcats
            diagram. If `category`, hover interaction take place
            per category. If `color`, hover interactions take place
            per color per category. If `dimension`, hover
            interactions take place across all categories per
            dimension.
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `count`, `probability`,
            `category`, `categorycount`, `colorcount` and
            `bandcolorcount`. Anything contained in tag `<extra>`
            is displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        labelfont
            Sets the font for the `dimension` labels.
        line
            :class:`plotly.graph_objects.parcats.Line` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        sortpaths
            Sets the path sorting algorithm. If `forward`, sort
            paths based on dimension categories from left to right.
            If `backward`, sort paths based on dimensions
            categories from right to left.
        stream
            :class:`plotly.graph_objects.parcats.Stream` instance
            or dict with compatible properties
        tickfont
            Sets the font for the `category` labels.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Parcats

        new_trace = Parcats(
            arrangement=arrangement,
            bundlecolors=bundlecolors,
            counts=counts,
            countssrc=countssrc,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            domain=domain,
            hoverinfo=hoverinfo,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            labelfont=labelfont,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            sortpaths=sortpaths,
            stream=stream,
            tickfont=tickfont,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_parcoords(
        self,
        customdata=None,
        customdatasrc=None,
        dimensions=None,
        dimensiondefaults=None,
        domain=None,
        ids=None,
        idssrc=None,
        labelangle=None,
        labelfont=None,
        labelside=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        rangefont=None,
        stream=None,
        tickfont=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Parcoords trace
        
        Parallel coordinates for multidimensional exploratory data
        analysis. The samples are specified in `dimensions`. The colors
        are set in `line.color`.

        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dimensions
            The dimensions (variables) of the parallel coordinates
            chart. 2..60 dimensions are supported.
        dimensiondefaults
            When used in a template (as
            layout.template.data.parcoords.dimensiondefaults), sets
            the default property values to use for elements of
            parcoords.dimensions
        domain
            :class:`plotly.graph_objects.parcoords.Domain` instance
            or dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        labelangle
            Sets the angle of the labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            labels vertically. Tilted labels with "labelangle" may
            be positioned better inside margins when
            `labelposition` is set to "bottom".
        labelfont
            Sets the font for the `dimension` labels.
        labelside
            Specifies the location of the `label`. "top" positions
            labels above, next to the title "bottom" positions
            labels below the graph Tilted labels with "labelangle"
            may be positioned better inside margins when
            `labelposition` is set to "bottom".
        line
            :class:`plotly.graph_objects.parcoords.Line` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        rangefont
            Sets the font for the `dimension` range values.
        stream
            :class:`plotly.graph_objects.parcoords.Stream` instance
            or dict with compatible properties
        tickfont
            Sets the font for the `dimension` tick values.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Parcoords

        new_trace = Parcoords(
            customdata=customdata,
            customdatasrc=customdatasrc,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            domain=domain,
            ids=ids,
            idssrc=idssrc,
            labelangle=labelangle,
            labelfont=labelfont,
            labelside=labelside,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            rangefont=rangefont,
            stream=stream,
            tickfont=tickfont,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_pie(
        self,
        automargin=None,
        customdata=None,
        customdatasrc=None,
        direction=None,
        dlabel=None,
        domain=None,
        hole=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        insidetextorientation=None,
        label0=None,
        labels=None,
        labelssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        pull=None,
        pullsrc=None,
        rotation=None,
        scalegroup=None,
        showlegend=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        title=None,
        titlefont=None,
        titleposition=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Pie trace
        
        A data visualized by the sectors of the pie is set in `values`.
        The sector labels are set in `labels`. The sector colors are
        set in `marker.colors`

        Parameters
        ----------
        automargin
            Determines whether outside text labels can push the
            margins.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        direction
            Specifies the direction at which succeeding sectors
            follow one another.
        dlabel
            Sets the label step. See `label0` for more info.
        domain
            :class:`plotly.graph_objects.pie.Domain` instance or
            dict with compatible properties
        hole
            Sets the fraction of the radius to cut out of the pie.
            Use this to make a donut chart.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.pie.Hoverlabel` instance
            or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `label`, `color`, `value`,
            `percent` and `text`. Anything contained in tag
            `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        insidetextorientation
            Controls the orientation of the text inside chart
            sectors. When set to "auto", text may be oriented in
            any direction in order to be as big as possible in the
            middle of a sector. The "horizontal" option orients
            text to be parallel with the bottom of the chart, and
            may make text smaller in order to achieve that goal.
            The "radial" option orients text along the radius of
            the sector. The "tangential" option orients text
            perpendicular to the radius of the sector.
        label0
            Alternate to `labels`. Builds a numeric set of labels.
            Use with `dlabel` where `label0` is the starting label
            and `dlabel` the step.
        labels
            Sets the sector labels. If `labels` entries are
            duplicated, we sum associated `values` or simply count
            occurrences if `values` is not provided. For other
            array attributes (including color) we use the first
            non-empty entry among all occurrences of the label.
        labelssrc
            Sets the source reference on Chart Studio Cloud for
            labels .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.pie.Marker` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            sector.
        pull
            Sets the fraction of larger radius to pull the sectors
            out from the center. This can be a constant to pull all
            slices apart from each other equally or an array to
            highlight one or more slices.
        pullsrc
            Sets the source reference on Chart Studio Cloud for
            pull .
        rotation
            Instead of the first slice starting at 12 o'clock,
            rotate to some other angle.
        scalegroup
            If there are multiple pie charts that should be sized
            according to their totals, link them by providing a
            non-empty group id here shared by every trace in the
            same group.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        sort
            Determines whether or not the sectors are reordered
            from largest to smallest.
        stream
            :class:`plotly.graph_objects.pie.Stream` instance or
            dict with compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Specifies the location of the `textinfo`.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `label`,
            `color`, `value`, `percent` and `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        title
            :class:`plotly.graph_objects.pie.Title` instance or
            dict with compatible properties
        titlefont
            Deprecated: Please use pie.title.font instead. Sets the
            font used for `title`. Note that the title's font used
            to be set by the now deprecated `titlefont` attribute.
        titleposition
            Deprecated: Please use pie.title.position instead.
            Specifies the location of the `title`. Note that the
            title's position used to be set by the now deprecated
            `titleposition` attribute.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        values
            Sets the values of the sectors. If omitted, we count
            occurrences of each label.
        valuessrc
            Sets the source reference on Chart Studio Cloud for
            values .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Pie

        new_trace = Pie(
            automargin=automargin,
            customdata=customdata,
            customdatasrc=customdatasrc,
            direction=direction,
            dlabel=dlabel,
            domain=domain,
            hole=hole,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            insidetextorientation=insidetextorientation,
            label0=label0,
            labels=labels,
            labelssrc=labelssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            pull=pull,
            pullsrc=pullsrc,
            rotation=rotation,
            scalegroup=scalegroup,
            showlegend=showlegend,
            sort=sort,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            title=title,
            titlefont=titlefont,
            titleposition=titleposition,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_pointcloud(
        self,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        indices=None,
        indicessrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbounds=None,
        xboundssrc=None,
        xsrc=None,
        xy=None,
        xysrc=None,
        y=None,
        yaxis=None,
        ybounds=None,
        yboundssrc=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Pointcloud trace
        
        The data visualized as a point cloud set in `x` and `y` using
        the WebGl plotting engine.

        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.pointcloud.Hoverlabel`
            instance or dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        indices
            A sequential value, 0..n, supply it to avoid creating
            this array inside plotting. If specified, it must be a
            typed `Int32Array` array. Its length must be equal to
            or greater than the number of points. For the best
            performance and memory use, create one large `indices`
            typed array that is guaranteed to be at least as long
            as the largest number of points during use, and reuse
            it on each `Plotly.restyle()` call.
        indicessrc
            Sets the source reference on Chart Studio Cloud for
            indices .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.pointcloud.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.pointcloud.Stream`
            instance or dict with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbounds
            Specify `xbounds` in the shape of `[xMin, xMax] to
            avoid looping through the `xy` typed array. Use it in
            conjunction with `xy` and `ybounds` for the performance
            benefits.
        xboundssrc
            Sets the source reference on Chart Studio Cloud for
            xbounds .
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        xy
            Faster alternative to specifying `x` and `y`
            separately. If supplied, it must be a typed
            `Float32Array` array that represents points such that
            `xy[i * 2] = x[i]` and `xy[i * 2 + 1] = y[i]`
        xysrc
            Sets the source reference on Chart Studio Cloud for  xy
            .
        y
            Sets the y coordinates.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybounds
            Specify `ybounds` in the shape of `[yMin, yMax] to
            avoid looping through the `xy` typed array. Use it in
            conjunction with `xy` and `xbounds` for the performance
            benefits.
        yboundssrc
            Sets the source reference on Chart Studio Cloud for
            ybounds .
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Pointcloud

        new_trace = Pointcloud(
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            indices=indices,
            indicessrc=indicessrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbounds=xbounds,
            xboundssrc=xboundssrc,
            xsrc=xsrc,
            xy=xy,
            xysrc=xysrc,
            y=y,
            yaxis=yaxis,
            ybounds=ybounds,
            yboundssrc=yboundssrc,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_sankey(
        self,
        arrangement=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        link=None,
        meta=None,
        metasrc=None,
        name=None,
        node=None,
        orientation=None,
        selectedpoints=None,
        stream=None,
        textfont=None,
        uid=None,
        uirevision=None,
        valueformat=None,
        valuesuffix=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Sankey trace
        
        Sankey plots for network flow data analysis. The nodes are
        specified in `nodes` and the links between sources and targets
        in `links`. The colors are set in `nodes[i].color` and
        `links[i].color`, otherwise defaults are used.

        Parameters
        ----------
        arrangement
            If value is `snap` (the default), the node arrangement
            is assisted by automatic snapping of elements to
            preserve space between nodes specified via `nodepad`.
            If value is `perpendicular`, the nodes can only move
            along a line perpendicular to the flow. If value is
            `freeform`, the nodes can freely move on the plane. If
            value is `fixed`, the nodes are stationary.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        domain
            :class:`plotly.graph_objects.sankey.Domain` instance or
            dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired. Note that this attribute is
            superseded by `node.hoverinfo` and `node.hoverinfo` for
            nodes and links respectively.
        hoverlabel
            :class:`plotly.graph_objects.sankey.Hoverlabel`
            instance or dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        link
            The links of the Sankey plot.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        node
            The nodes of the Sankey plot.
        orientation
            Sets the orientation of the Sankey diagram.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        stream
            :class:`plotly.graph_objects.sankey.Stream` instance or
            dict with compatible properties
        textfont
            Sets the font for node labels
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        valueformat
            Sets the value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        valuesuffix
            Adds a unit to follow the value in the hover tooltip.
            Add a space if a separation is necessary from the
            value.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Sankey

        new_trace = Sankey(
            arrangement=arrangement,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            link=link,
            meta=meta,
            metasrc=metasrc,
            name=name,
            node=node,
            orientation=orientation,
            selectedpoints=selectedpoints,
            stream=stream,
            textfont=textfont,
            uid=uid,
            uirevision=uirevision,
            valueformat=valueformat,
            valuesuffix=valuesuffix,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatter(
        self,
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        fill=None,
        fillcolor=None,
        groupnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        orientation=None,
        r=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stackgaps=None,
        stackgroup=None,
        stream=None,
        t=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        tsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Scatter trace
        
        The scatter trace type encompasses line charts, scatter charts,
        text charts, and bubble charts. The data visualized as scatter
        point or lines is set in `x` and `y`. Text (appearing either on
        the chart or on hover only) is via `text`. Bubble charts are
        achieved by setting `marker.size` and/or `marker.color` to
        numerical arrays.

        Parameters
        ----------
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            :class:`plotly.graph_objects.scatter.ErrorX` instance
            or dict with compatible properties
        error_y
            :class:`plotly.graph_objects.scatter.ErrorY` instance
            or dict with compatible properties
        fill
            Sets the area to fill with a solid color. Defaults to
            "none" unless this trace is stacked, then it gets
            "tonexty" ("tonextx") if `orientation` is "v" ("h") Use
            with `fillcolor` if not "none". "tozerox" and "tozeroy"
            fill to x=0 and y=0 respectively. "tonextx" and
            "tonexty" fill between the endpoints of this trace and
            the endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other. Traces in a `stackgroup` will only fill to (or
            be filled to) other traces in the same group. With
            multiple `stackgroup`s or some traces stacked and some
            not, if fill-linked traces are not already consecutive,
            the later ones will be pushed down in the drawing
            order.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        groupnorm
            Only relevant when `stackgroup` is used, and only the
            first `groupnorm` found in the `stackgroup` will be
            used - including if `visible` is "legendonly" but not
            if it is `false`. Sets the normalization for the sum of
            this `stackgroup`. With "fraction", the value of each
            trace at each location is divided by the sum of all
            trace values at that location. "percent" is the same
            but multiplied by 100 to show percentages. If there are
            multiple subplots, or multiple `stackgroup`s on one
            subplot, each will be normalized within its own set.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scatter.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scatter.Line` instance or
            dict with compatible properties
        marker
            :class:`plotly.graph_objects.scatter.Marker` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        orientation
            Only relevant when `stackgroup` is used, and only the
            first `orientation` found in the `stackgroup` will be
            used - including if `visible` is "legendonly" but not
            if it is `false`. Sets the stacking direction. With "v"
            ("h"), the y (x) values of subsequent traces are added.
            Also affects the default value of `fill`.
        r
            r coordinates in scatter traces are deprecated!Please
            switch to the "scatterpolar" trace type.Sets the radial
            coordinatesfor legacy polar chart only.
        rsrc
            Sets the source reference on Chart Studio Cloud for  r
            .
        selected
            :class:`plotly.graph_objects.scatter.Selected` instance
            or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stackgaps
            Only relevant when `stackgroup` is used, and only the
            first `stackgaps` found in the `stackgroup` will be
            used - including if `visible` is "legendonly" but not
            if it is `false`. Determines how we handle locations at
            which other traces in this group have data but this one
            does not. With *infer zero* we insert a zero at these
            locations. With "interpolate" we linearly interpolate
            between existing values, and extrapolate a constant
            beyond the existing values.
        stackgroup
            Set several scatter traces (on the same subplot) to the
            same stackgroup in order to add their y values (or
            their x values if `orientation` is "h"). If blank or
            omitted this trace will not be stacked. Stacking also
            turns `fill` on by default, using "tonexty" ("tonextx")
            if `orientation` is "h" ("v") and sets the default
            `mode` to "lines" irrespective of point count. You can
            only stack on a numeric (linear or log) axis. Traces in
            a `stackgroup` will only fill to (or be filled to)
            other traces in the same group. With multiple
            `stackgroup`s or some traces stacked and some not, if
            fill-linked traces are not already consecutive, the
            later ones will be pushed down in the drawing order.
        stream
            :class:`plotly.graph_objects.scatter.Stream` instance
            or dict with compatible properties
        t
            t coordinates in scatter traces are deprecated!Please
            switch to the "scatterpolar" trace type.Sets the
            angular coordinatesfor legacy polar chart only.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        tsrc
            Sets the source reference on Chart Studio Cloud for  t
            .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scatter.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scatter

        new_trace = Scatter(
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            fill=fill,
            fillcolor=fillcolor,
            groupnorm=groupnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            orientation=orientation,
            r=r,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stackgaps=stackgaps,
            stackgroup=stackgroup,
            stream=stream,
            t=t,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            tsrc=tsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_scatter3d(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        error_x=None,
        error_y=None,
        error_z=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        projection=None,
        scene=None,
        showlegend=None,
        stream=None,
        surfaceaxis=None,
        surfacecolor=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scatter3d trace
        
        The data visualized as scatter point or lines in 3D dimension
        is set in `x`, `y`, `z`. Text (appearing either on the chart or
        on hover only) is via `text`. Bubble charts are achieved by
        setting `marker.size` and/or `marker.color` Projections are
        achieved via `projection`. Surface fills are achieved via
        `surfaceaxis`.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        error_x
            :class:`plotly.graph_objects.scatter3d.ErrorX` instance
            or dict with compatible properties
        error_y
            :class:`plotly.graph_objects.scatter3d.ErrorY` instance
            or dict with compatible properties
        error_z
            :class:`plotly.graph_objects.scatter3d.ErrorZ` instance
            or dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scatter3d.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets text elements associated with each (x,y,z)
            triplet. If a single string, the same string appears
            over all the data points. If an array of string, the
            items are mapped in order to the this trace's (x,y,z)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scatter3d.Line` instance
            or dict with compatible properties
        marker
            :class:`plotly.graph_objects.scatter3d.Marker` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        projection
            :class:`plotly.graph_objects.scatter3d.Projection`
            instance or dict with compatible properties
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scatter3d.Stream` instance
            or dict with compatible properties
        surfaceaxis
            If "-1", the scatter points are not fill with a surface
            If 0, 1, 2, the scatter points are filled with a
            Delaunay surface about the x, y, z respectively.
        surfacecolor
            Sets the surface fill color.
        text
            Sets text elements associated with each (x,y,z)
            triplet. If a single string, the same string appears
            over all the data points. If an array of string, the
            items are mapped in order to the this trace's (x,y,z)
            coordinates. If trace `hoverinfo` contains a "text"
            flag and "hovertext" is not set, these elements will be
            seen in the hover labels.
        textfont
            :class:`plotly.graph_objects.scatter3d.Textfont`
            instance or dict with compatible properties
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the z coordinates.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scatter3d

        new_trace = Scatter3d(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            error_x=error_x,
            error_y=error_y,
            error_z=error_z,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            projection=projection,
            scene=scene,
            showlegend=showlegend,
            stream=stream,
            surfaceaxis=surfaceaxis,
            surfacecolor=surfacecolor,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scattercarpet(
        self,
        a=None,
        asrc=None,
        b=None,
        bsrc=None,
        carpet=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        xaxis=None,
        yaxis=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Scattercarpet trace
        
        Plots a scatter trace on either the first carpet axis or the
        carpet axis with a matching `carpet` attribute.

        Parameters
        ----------
        a
            Sets the a-axis coordinates.
        asrc
            Sets the source reference on Chart Studio Cloud for  a
            .
        b
            Sets the b-axis coordinates.
        bsrc
            Sets the source reference on Chart Studio Cloud for  b
            .
        carpet
            An identifier for this carpet, so that `scattercarpet`
            and `contourcarpet` traces can specify a carpet plot on
            which they lie
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". scatterternary has a subset
            of the options available to scatter. "toself" connects
            the endpoints of the trace (or each segment of the
            trace if it has gaps) into a closed shape. "tonext"
            fills the space between two traces if one completely
            encloses the other (eg consecutive contour lines), and
            behaves like "toself" if there is no trace before it.
            "tonext" should not be used if one trace does not
            enclose the other.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scattercarpet.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (a,b)
            point. If a single string, the same string appears over
            all the data points. If an array of strings, the items
            are mapped in order to the the data points in (a,b). To
            be seen, trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scattercarpet.Line`
            instance or dict with compatible properties
        marker
            :class:`plotly.graph_objects.scattercarpet.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            :class:`plotly.graph_objects.scattercarpet.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scattercarpet.Stream`
            instance or dict with compatible properties
        text
            Sets text elements associated with each (a,b) point. If
            a single string, the same string appears over all the
            data points. If an array of strings, the items are
            mapped in order to the the data points in (a,b). If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `a`, `b` and
            `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scattercarpet.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scattercarpet

        new_trace = Scattercarpet(
            a=a,
            asrc=asrc,
            b=b,
            bsrc=bsrc,
            carpet=carpet,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            xaxis=xaxis,
            yaxis=yaxis,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_scattergeo(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        featureidkey=None,
        fill=None,
        fillcolor=None,
        geo=None,
        geojson=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legendgroup=None,
        line=None,
        locationmode=None,
        locations=None,
        locationssrc=None,
        lon=None,
        lonsrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scattergeo trace
        
        The data visualized as scatter point or lines on a geographic
        map is provided either by longitude/latitude pairs in `lon` and
        `lat` respectively or by geographic location IDs or names in
        `locations`.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        featureidkey
            Sets the key in GeoJSON features which is used as id to
            match the items included in the `locations` array. Only
            has an effect when `geojson` is set. Support nested
            property, for example "properties.name".
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        geo
            Sets a reference between this trace's geospatial
            coordinates and a geographic map. If "geo" (the default
            value), the geospatial coordinates refer to
            `layout.geo`. If "geo2", the geospatial coordinates
            refer to `layout.geo2`, and so on.
        geojson
            Sets optional GeoJSON data associated with this trace.
            If not given, the features on the base map are used
            when `locations` is set. It can be set as a valid
            GeoJSON object or as a URL string. Note that we only
            accept GeoJSONs of type "FeatureCollection" or
            "Feature" with geometries of type "Polygon" or
            "MultiPolygon".
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scattergeo.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (lon,lat)
            pair or item in `locations`. If a single string, the
            same string appears over all the data points. If an
            array of string, the items are mapped in order to the
            this trace's (lon,lat) or `locations` coordinates. To
            be seen, trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        lat
            Sets the latitude coordinates (in degrees North).
        latsrc
            Sets the source reference on Chart Studio Cloud for
            lat .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scattergeo.Line` instance
            or dict with compatible properties
        locationmode
            Determines the set of locations used to match entries
            in `locations` to regions on the map. Values "ISO-3",
            "USA-states", *country names* correspond to features on
            the base map and value "geojson-id" corresponds to
            features from a custom GeoJSON linked to the `geojson`
            attribute.
        locations
            Sets the coordinates via location IDs or names.
            Coordinates correspond to the centroid of each location
            given. See `locationmode` for more info.
        locationssrc
            Sets the source reference on Chart Studio Cloud for
            locations .
        lon
            Sets the longitude coordinates (in degrees East).
        lonsrc
            Sets the source reference on Chart Studio Cloud for
            lon .
        marker
            :class:`plotly.graph_objects.scattergeo.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            :class:`plotly.graph_objects.scattergeo.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scattergeo.Stream`
            instance or dict with compatible properties
        text
            Sets text elements associated with each (lon,lat) pair
            or item in `locations`. If a single string, the same
            string appears over all the data points. If an array of
            string, the items are mapped in order to the this
            trace's (lon,lat) or `locations` coordinates. If trace
            `hoverinfo` contains a "text" flag and "hovertext" is
            not set, these elements will be seen in the hover
            labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `lat`, `lon`,
            `location` and `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scattergeo.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scattergeo

        new_trace = Scattergeo(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            featureidkey=featureidkey,
            fill=fill,
            fillcolor=fillcolor,
            geo=geo,
            geojson=geojson,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legendgroup=legendgroup,
            line=line,
            locationmode=locationmode,
            locations=locations,
            locationssrc=locationssrc,
            lon=lon,
            lonsrc=lonsrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scattergl(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Scattergl trace
        
        The data visualized as scatter point or lines is set in `x` and
        `y` using the WebGL plotting engine. Bubble charts are achieved
        by setting `marker.size` and/or `marker.color` to a numerical
        arrays.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            :class:`plotly.graph_objects.scattergl.ErrorX` instance
            or dict with compatible properties
        error_y
            :class:`plotly.graph_objects.scattergl.ErrorY` instance
            or dict with compatible properties
        fill
            Sets the area to fill with a solid color. Defaults to
            "none" unless this trace is stacked, then it gets
            "tonexty" ("tonextx") if `orientation` is "v" ("h") Use
            with `fillcolor` if not "none". "tozerox" and "tozeroy"
            fill to x=0 and y=0 respectively. "tonextx" and
            "tonexty" fill between the endpoints of this trace and
            the endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other. Traces in a `stackgroup` will only fill to (or
            be filled to) other traces in the same group. With
            multiple `stackgroup`s or some traces stacked and some
            not, if fill-linked traces are not already consecutive,
            the later ones will be pushed down in the drawing
            order.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scattergl.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scattergl.Line` instance
            or dict with compatible properties
        marker
            :class:`plotly.graph_objects.scattergl.Marker` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            :class:`plotly.graph_objects.scattergl.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scattergl.Stream` instance
            or dict with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scattergl.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scattergl

        new_trace = Scattergl(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_scattermapbox(
        self,
        below=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legendgroup=None,
        line=None,
        lon=None,
        lonsrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scattermapbox trace
        
        The data visualized as scatter point, lines or marker symbols
        on a Mapbox GL geographic map is provided by longitude/latitude
        pairs in `lon` and `lat`.

        Parameters
        ----------
        below
            Determines if this scattermapbox trace's layers are to
            be inserted before the layer with the specified ID. By
            default, scattermapbox layers are inserted above all
            the base layers. To place the scattermapbox layers
            above every other layer, set `below` to "''".
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scattermapbox.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (lon,lat)
            pair If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (lon,lat)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        lat
            Sets the latitude coordinates (in degrees North).
        latsrc
            Sets the source reference on Chart Studio Cloud for
            lat .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scattermapbox.Line`
            instance or dict with compatible properties
        lon
            Sets the longitude coordinates (in degrees East).
        lonsrc
            Sets the source reference on Chart Studio Cloud for
            lon .
        marker
            :class:`plotly.graph_objects.scattermapbox.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            :class:`plotly.graph_objects.scattermapbox.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scattermapbox.Stream`
            instance or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a mapbox subplot. If "mapbox" (the default value),
            the data refer to `layout.mapbox`. If "mapbox2", the
            data refer to `layout.mapbox2`, and so on.
        text
            Sets text elements associated with each (lon,lat) pair
            If a single string, the same string appears over all
            the data points. If an array of string, the items are
            mapped in order to the this trace's (lon,lat)
            coordinates. If trace `hoverinfo` contains a "text"
            flag and "hovertext" is not set, these elements will be
            seen in the hover labels.
        textfont
            Sets the icon text font (color=mapbox.layer.paint.text-
            color, size=mapbox.layer.layout.text-size). Has an
            effect only when `type` is set to "symbol".
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `lat`, `lon`
            and `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scattermapbox.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scattermapbox

        new_trace = Scattermapbox(
            below=below,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legendgroup=legendgroup,
            line=line,
            lon=lon,
            lonsrc=lonsrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterpolar(
        self,
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scatterpolar trace
        
        The scatterpolar trace type encompasses line charts, scatter
        charts, text charts, and bubble charts in polar coordinates.
        The data visualized as scatter point or lines is set in `r`
        (radial) and `theta` (angular) coordinates Text (appearing
        either on the chart or on hover only) is via `text`. Bubble
        charts are achieved by setting `marker.size` and/or
        `marker.color` to numerical arrays.

        Parameters
        ----------
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". scatterpolar has a subset of
            the options available to scatter. "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scatterpolar.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scatterpolar.Line`
            instance or dict with compatible properties
        marker
            :class:`plotly.graph_objects.scatterpolar.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on Chart Studio Cloud for  r
            .
        selected
            :class:`plotly.graph_objects.scatterpolar.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scatterpolar.Stream`
            instance or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `r`, `theta`
            and `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on Chart Studio Cloud for
            theta .
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scatterpolar.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scatterpolar

        new_trace = Scatterpolar(
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterpolargl(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scatterpolargl trace
        
        The scatterpolargl trace type encompasses line charts, scatter
        charts, and bubble charts in polar coordinates using the WebGL
        plotting engine. The data visualized as scatter point or lines
        is set in `r` (radial) and `theta` (angular) coordinates Bubble
        charts are achieved by setting `marker.size` and/or
        `marker.color` to numerical arrays.

        Parameters
        ----------
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        fill
            Sets the area to fill with a solid color. Defaults to
            "none" unless this trace is stacked, then it gets
            "tonexty" ("tonextx") if `orientation` is "v" ("h") Use
            with `fillcolor` if not "none". "tozerox" and "tozeroy"
            fill to x=0 and y=0 respectively. "tonextx" and
            "tonexty" fill between the endpoints of this trace and
            the endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other. Traces in a `stackgroup` will only fill to (or
            be filled to) other traces in the same group. With
            multiple `stackgroup`s or some traces stacked and some
            not, if fill-linked traces are not already consecutive,
            the later ones will be pushed down in the drawing
            order.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scatterpolargl.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scatterpolargl.Line`
            instance or dict with compatible properties
        marker
            :class:`plotly.graph_objects.scatterpolargl.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on Chart Studio Cloud for  r
            .
        selected
            :class:`plotly.graph_objects.scatterpolargl.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scatterpolargl.Stream`
            instance or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `r`, `theta`
            and `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on Chart Studio Cloud for
            theta .
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scatterpolargl.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scatterpolargl

        new_trace = Scatterpolargl(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterternary(
        self,
        a=None,
        asrc=None,
        b=None,
        bsrc=None,
        c=None,
        cliponaxis=None,
        connectgaps=None,
        csrc=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        sum=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Scatterternary trace
        
        Provides similar functionality to the "scatter" type but on a
        ternary phase diagram. The data is provided by at least two
        arrays out of `a`, `b`, `c` triplets.

        Parameters
        ----------
        a
            Sets the quantity of component `a` in each data point.
            If `a`, `b`, and `c` are all provided, they need not be
            normalized, only the relative values matter. If only
            two arrays are provided they must be normalized to
            match `ternary<i>.sum`.
        asrc
            Sets the source reference on Chart Studio Cloud for  a
            .
        b
            Sets the quantity of component `a` in each data point.
            If `a`, `b`, and `c` are all provided, they need not be
            normalized, only the relative values matter. If only
            two arrays are provided they must be normalized to
            match `ternary<i>.sum`.
        bsrc
            Sets the source reference on Chart Studio Cloud for  b
            .
        c
            Sets the quantity of component `a` in each data point.
            If `a`, `b`, and `c` are all provided, they need not be
            normalized, only the relative values matter. If only
            two arrays are provided they must be normalized to
            match `ternary<i>.sum`.
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        csrc
            Sets the source reference on Chart Studio Cloud for  c
            .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". scatterternary has a subset
            of the options available to scatter. "toself" connects
            the endpoints of the trace (or each segment of the
            trace if it has gaps) into a closed shape. "tonext"
            fills the space between two traces if one completely
            encloses the other (eg consecutive contour lines), and
            behaves like "toself" if there is no trace before it.
            "tonext" should not be used if one trace does not
            enclose the other.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.scatterternary.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (a,b,c)
            point. If a single string, the same string appears over
            all the data points. If an array of strings, the items
            are mapped in order to the the data points in (a,b,c).
            To be seen, trace `hoverinfo` must contain a "text"
            flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.scatterternary.Line`
            instance or dict with compatible properties
        marker
            :class:`plotly.graph_objects.scatterternary.Marker`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            :class:`plotly.graph_objects.scatterternary.Selected`
            instance or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.scatterternary.Stream`
            instance or dict with compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a ternary subplot. If "ternary" (the default
            value), the data refer to `layout.ternary`. If
            "ternary2", the data refer to `layout.ternary2`, and so
            on.
        sum
            The number each triplet should sum to, if only two of
            `a`, `b`, and `c` are provided. This overrides
            `ternary<i>.sum` to normalize this specific trace, but
            does not affect the values displayed on the axes. 0 (or
            missing) means to use ternary<i>.sum
        text
            Sets text elements associated with each (a,b,c) point.
            If a single string, the same string appears over all
            the data points. If an array of strings, the items are
            mapped in order to the the data points in (a,b,c). If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `a`, `b`, `c`
            and `text`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scatterternary.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Scatterternary

        new_trace = Scatterternary(
            a=a,
            asrc=asrc,
            b=b,
            bsrc=bsrc,
            c=c,
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            csrc=csrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            sum=sum,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_splom(
        self,
        customdata=None,
        customdatasrc=None,
        diagonal=None,
        dimensions=None,
        dimensiondefaults=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showlowerhalf=None,
        showupperhalf=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        xaxes=None,
        yaxes=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Splom trace
        
        Splom traces generate scatter plot matrix visualizations. Each
        splom `dimensions` items correspond to a generated axis. Values
        for each of those dimensions are set in `dimensions[i].values`.
        Splom traces support all `scattergl` marker style attributes.
        Specify `layout.grid` attributes and/or layout x-axis and
        y-axis attributes for more control over the axis positioning
        and style.

        Parameters
        ----------
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        diagonal
            :class:`plotly.graph_objects.splom.Diagonal` instance
            or dict with compatible properties
        dimensions
            A tuple of
            :class:`plotly.graph_objects.splom.Dimension` instances
            or dicts with compatible properties
        dimensiondefaults
            When used in a template (as
            layout.template.data.splom.dimensiondefaults), sets the
            default property values to use for elements of
            splom.dimensions
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.splom.Hoverlabel` instance
            or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            :class:`plotly.graph_objects.splom.Marker` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selected
            :class:`plotly.graph_objects.splom.Selected` instance
            or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showlowerhalf
            Determines whether or not subplots on the lower half
            from the diagonal are displayed.
        showupperhalf
            Determines whether or not subplots on the upper half
            from the diagonal are displayed.
        stream
            :class:`plotly.graph_objects.splom.Stream` instance or
            dict with compatible properties
        text
            Sets text elements associated with each (x,y) pair to
            appear on hover. If a single string, the same string
            appears over all the data points. If an array of
            string, the items are mapped in order to the this
            trace's (x,y) coordinates.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.splom.Unselected` instance
            or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        xaxes
            Sets the list of x axes corresponding to dimensions of
            this splom trace. By default, a splom will match the
            first N xaxes where N is the number of input
            dimensions. Note that, in case where `diagonal.visible`
            is false and `showupperhalf` or `showlowerhalf` is
            false, this splom trace will generate one less x-axis
            and one less y-axis.
        yaxes
            Sets the list of y axes corresponding to dimensions of
            this splom trace. By default, a splom will match the
            first N yaxes where N is the number of input
            dimensions. Note that, in case where `diagonal.visible`
            is false and `showupperhalf` or `showlowerhalf` is
            false, this splom trace will generate one less x-axis
            and one less y-axis.
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Splom

        new_trace = Splom(
            customdata=customdata,
            customdatasrc=customdatasrc,
            diagonal=diagonal,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showlowerhalf=showlowerhalf,
            showupperhalf=showupperhalf,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            xaxes=xaxes,
            yaxes=yaxes,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_streamtube(
        self,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        lighting=None,
        lightposition=None,
        maxdisplayed=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        sizeref=None,
        starts=None,
        stream=None,
        text=None,
        u=None,
        uid=None,
        uirevision=None,
        usrc=None,
        v=None,
        visible=None,
        vsrc=None,
        w=None,
        wsrc=None,
        x=None,
        xsrc=None,
        y=None,
        ysrc=None,
        z=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Streamtube trace
        
        Use a streamtube trace to visualize flow in a vector field.
        Specify a vector field using 6 1D arrays of equal length, 3
        position arrays `x`, `y` and `z` and 3 vector component arrays
        `u`, `v`, and `w`.  By default, the tubes' starting positions
        will be cut from the vector field's x-z plane at its minimum y
        value. To specify your own starting position, use attributes
        `starts.x`, `starts.y` and `starts.z`. The color is encoded by
        the norm of (u, v, w), and the local radius by the divergence
        of (u, v, w).

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here u/v/w norm) or the
            bounds set in `cmin` and `cmax`  Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as u/v/w norm. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as u/v/w norm and if set, `cmax`
            must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.streamtube.ColorBar`
            instance or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.streamtube.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `tubex`, `tubey`, `tubez`,
            `tubeu`, `tubev`, `tubew`, `norm` and `divergence`.
            Anything contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lighting
            :class:`plotly.graph_objects.streamtube.Lighting`
            instance or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.streamtube.Lightposition`
            instance or dict with compatible properties
        maxdisplayed
            The maximum number of displayed segments in a
            streamtube.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        sizeref
            The scaling factor for the streamtubes. The default is
            1, which avoids two max divergence tubes from touching
            at adjacent starting positions.
        starts
            :class:`plotly.graph_objects.streamtube.Starts`
            instance or dict with compatible properties
        stream
            :class:`plotly.graph_objects.streamtube.Stream`
            instance or dict with compatible properties
        text
            Sets a text element associated with this trace. If
            trace `hoverinfo` contains a "text" flag, this text
            element will be seen in all hover labels. Note that
            streamtube traces do not support array `text` values.
        u
            Sets the x components of the vector field.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        usrc
            Sets the source reference on Chart Studio Cloud for  u
            .
        v
            Sets the y components of the vector field.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        vsrc
            Sets the source reference on Chart Studio Cloud for  v
            .
        w
            Sets the z components of the vector field.
        wsrc
            Sets the source reference on Chart Studio Cloud for  w
            .
        x
            Sets the x coordinates of the vector field.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates of the vector field.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the z coordinates of the vector field.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Streamtube

        new_trace = Streamtube(
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            lighting=lighting,
            lightposition=lightposition,
            maxdisplayed=maxdisplayed,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            sizeref=sizeref,
            starts=starts,
            stream=stream,
            text=text,
            u=u,
            uid=uid,
            uirevision=uirevision,
            usrc=usrc,
            v=v,
            visible=visible,
            vsrc=vsrc,
            w=w,
            wsrc=wsrc,
            x=x,
            xsrc=xsrc,
            y=y,
            ysrc=ysrc,
            z=z,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_sunburst(
        self,
        branchvalues=None,
        count=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        insidetextorientation=None,
        labels=None,
        labelssrc=None,
        leaf=None,
        level=None,
        marker=None,
        maxdepth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        parents=None,
        parentssrc=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Sunburst trace
        
        Visualize hierarchal data spanning outward radially from root
        to leaves. The sunburst sectors are determined by the entries
        in "labels" or "ids" and in "parents".

        Parameters
        ----------
        branchvalues
            Determines how the items in `values` are summed. When
            set to "total", items in `values` are taken to be value
            of all its descendants. When set to "remainder", items
            in `values` corresponding to the root and the branches
            sectors are taken to be the extra part not part of the
            sum of the values at their leaves.
        count
            Determines default for `values` when it is not
            provided, by inferring a 1 for each of the "leaves"
            and/or "branches", otherwise 0.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        domain
            :class:`plotly.graph_objects.sunburst.Domain` instance
            or dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.sunburst.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `currentPath`, `root`,
            `entry`, `percentRoot`, `percentEntry` and
            `percentParent`. Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        insidetextorientation
            Controls the orientation of the text inside chart
            sectors. When set to "auto", text may be oriented in
            any direction in order to be as big as possible in the
            middle of a sector. The "horizontal" option orients
            text to be parallel with the bottom of the chart, and
            may make text smaller in order to achieve that goal.
            The "radial" option orients text along the radius of
            the sector. The "tangential" option orients text
            perpendicular to the radius of the sector.
        labels
            Sets the labels of each of the sectors.
        labelssrc
            Sets the source reference on Chart Studio Cloud for
            labels .
        leaf
            :class:`plotly.graph_objects.sunburst.Leaf` instance or
            dict with compatible properties
        level
            Sets the level from which this trace hierarchy is
            rendered. Set `level` to `''` to start from the root
            node in the hierarchy. Must be an "id" if `ids` is
            filled in, otherwise plotly attempts to find a matching
            item in `labels`.
        marker
            :class:`plotly.graph_objects.sunburst.Marker` instance
            or dict with compatible properties
        maxdepth
            Sets the number of rendered sectors from any given
            `level`. Set `maxdepth` to "-1" to render all the
            levels in the hierarchy.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            sector. This option refers to the root of the hierarchy
            presented at the center of a sunburst graph. Please
            note that if a hierarchy has multiple root nodes, this
            option won't have any effect and `insidetextfont` would
            be used.
        parents
            Sets the parent sectors for each of the sectors. Empty
            string items '' are understood to reference the root
            node in the hierarchy. If `ids` is filled, `parents`
            items are understood to be "ids" themselves. When `ids`
            is not set, plotly attempts to find matching items in
            `labels`, but beware they must be unique.
        parentssrc
            Sets the source reference on Chart Studio Cloud for
            parents .
        sort
            Determines whether or not the sectors are reordered
            from largest to smallest.
        stream
            :class:`plotly.graph_objects.sunburst.Stream` instance
            or dict with compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables
            `currentPath`, `root`, `entry`, `percentRoot`,
            `percentEntry`, `percentParent`, `label` and `value`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        values
            Sets the values associated with each of the sectors.
            Use with `branchvalues` to determine how the values are
            summed.
        valuessrc
            Sets the source reference on Chart Studio Cloud for
            values .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Sunburst

        new_trace = Sunburst(
            branchvalues=branchvalues,
            count=count,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            insidetextorientation=insidetextorientation,
            labels=labels,
            labelssrc=labelssrc,
            leaf=leaf,
            level=level,
            marker=marker,
            maxdepth=maxdepth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            parents=parents,
            parentssrc=parentssrc,
            sort=sort,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_surface(
        self,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        hidesurface=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        opacityscale=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        stream=None,
        surfacecolor=None,
        surfacecolorsrc=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Surface trace
        
        The data the describes the coordinates of the surface is set in
        `z`. Data in `z` should be a 2D list. Coordinates in `x` and
        `y` can either be 1D lists or 2D lists (e.g. to graph
        parametric surfaces). If not provided in `x` and `y`, the x and
        y coordinates are assumed to be linear starting at 0 with a
        unit step. The color scale corresponds to the `z` values by
        default. For custom color scales, use `surfacecolor` which
        should be a 2D list, where its bounds can be controlled using
        `cmin` and `cmax`.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here z or surfacecolor)
            or the bounds set in `cmin` and `cmax`  Defaults to
            `false` when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as z or surfacecolor and if set,
            `cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as z or surfacecolor.
            Has no effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as z or surfacecolor and if set,
            `cmax` must be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.surface.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data are filled in.
        contours
            :class:`plotly.graph_objects.surface.Contours` instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        hidesurface
            Determines whether or not a surface is drawn. For
            example, set `hidesurface` to False `contours.x.show`
            to True and `contours.y.show` to True to draw a wire
            frame plot.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.surface.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lighting
            :class:`plotly.graph_objects.surface.Lighting` instance
            or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.surface.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        opacityscale
            Sets the opacityscale. The opacityscale must be an
            array containing arrays mapping a normalized value to
            an opacity value. At minimum, a mapping for the lowest
            (0) and highest (1) values are required. For example,
            `[[0, 1], [0.5, 0.2], [1, 1]]` means that higher/lower
            values would have higher opacity values and those in
            the middle would be more transparent Alternatively,
            `opacityscale` may be a palette name string of the
            following list: 'min', 'max', 'extremes' and 'uniform'.
            The default is 'uniform'.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.surface.Stream` instance
            or dict with compatible properties
        surfacecolor
            Sets the surface color values, used for setting a color
            scale independent of `z`.
        surfacecolorsrc
            Sets the source reference on Chart Studio Cloud for
            surfacecolor .
        text
            Sets the text elements associated with each z value. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the z coordinates.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Surface

        new_trace = Surface(
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hidesurface=hidesurface,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legendgroup=legendgroup,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            opacityscale=opacityscale,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            surfacecolor=surfacecolor,
            surfacecolorsrc=surfacecolorsrc,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_table(
        self,
        cells=None,
        columnorder=None,
        columnordersrc=None,
        columnwidth=None,
        columnwidthsrc=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        header=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        meta=None,
        metasrc=None,
        name=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Table trace
        
        Table view for detailed data viewing. The data are arranged in
        a grid of rows and columns. Most styling can be specified for
        columns, rows or individual cells. Table is using a column-
        major order, ie. the grid is represented as a vector of column
        vectors.

        Parameters
        ----------
        cells
            :class:`plotly.graph_objects.table.Cells` instance or
            dict with compatible properties
        columnorder
            Specifies the rendered order of the data columns; for
            example, a value `2` at position `0` means that column
            index `0` in the data will be rendered as the third
            column, as columns have an index base of zero.
        columnordersrc
            Sets the source reference on Chart Studio Cloud for
            columnorder .
        columnwidth
            The width of columns expressed as a ratio. Columns fill
            the available width in proportion of their specified
            column widths.
        columnwidthsrc
            Sets the source reference on Chart Studio Cloud for
            columnwidth .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        domain
            :class:`plotly.graph_objects.table.Domain` instance or
            dict with compatible properties
        header
            :class:`plotly.graph_objects.table.Header` instance or
            dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.table.Hoverlabel` instance
            or dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        stream
            :class:`plotly.graph_objects.table.Stream` instance or
            dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Table

        new_trace = Table(
            cells=cells,
            columnorder=columnorder,
            columnordersrc=columnordersrc,
            columnwidth=columnwidth,
            columnwidthsrc=columnwidthsrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            header=header,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_treemap(
        self,
        branchvalues=None,
        count=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        labels=None,
        labelssrc=None,
        level=None,
        marker=None,
        maxdepth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        parents=None,
        parentssrc=None,
        pathbar=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        tiling=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Treemap trace
        
        Visualize hierarchal data from leaves (and/or outer branches)
        towards root with rectangles. The treemap sectors are
        determined by the entries in "labels" or "ids" and in
        "parents".

        Parameters
        ----------
        branchvalues
            Determines how the items in `values` are summed. When
            set to "total", items in `values` are taken to be value
            of all its descendants. When set to "remainder", items
            in `values` corresponding to the root and the branches
            sectors are taken to be the extra part not part of the
            sum of the values at their leaves.
        count
            Determines default for `values` when it is not
            provided, by inferring a 1 for each of the "leaves"
            and/or "branches", otherwise 0.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        domain
            :class:`plotly.graph_objects.treemap.Domain` instance
            or dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.treemap.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `currentPath`, `root`,
            `entry`, `percentRoot`, `percentEntry` and
            `percentParent`. Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the
            sector.
        labels
            Sets the labels of each of the sectors.
        labelssrc
            Sets the source reference on Chart Studio Cloud for
            labels .
        level
            Sets the level from which this trace hierarchy is
            rendered. Set `level` to `''` to start from the root
            node in the hierarchy. Must be an "id" if `ids` is
            filled in, otherwise plotly attempts to find a matching
            item in `labels`.
        marker
            :class:`plotly.graph_objects.treemap.Marker` instance
            or dict with compatible properties
        maxdepth
            Sets the number of rendered sectors from any given
            `level`. Set `maxdepth` to "-1" to render all the
            levels in the hierarchy.
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            sector. This option refers to the root of the hierarchy
            presented on top left corner of a treemap graph. Please
            note that if a hierarchy has multiple root nodes, this
            option won't have any effect and `insidetextfont` would
            be used.
        parents
            Sets the parent sectors for each of the sectors. Empty
            string items '' are understood to reference the root
            node in the hierarchy. If `ids` is filled, `parents`
            items are understood to be "ids" themselves. When `ids`
            is not set, plotly attempts to find matching items in
            `labels`, but beware they must be unique.
        parentssrc
            Sets the source reference on Chart Studio Cloud for
            parents .
        pathbar
            :class:`plotly.graph_objects.treemap.Pathbar` instance
            or dict with compatible properties
        sort
            Determines whether or not the sectors are reordered
            from largest to smallest.
        stream
            :class:`plotly.graph_objects.treemap.Stream` instance
            or dict with compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will be seen on the chart. If trace `hoverinfo`
            contains a "text" flag and "hovertext" is not set,
            these elements will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Sets the positions of the `text` elements.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables
            `currentPath`, `root`, `entry`, `percentRoot`,
            `percentEntry`, `percentParent`, `label` and `value`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        tiling
            :class:`plotly.graph_objects.treemap.Tiling` instance
            or dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        values
            Sets the values associated with each of the sectors.
            Use with `branchvalues` to determine how the values are
            summed.
        valuessrc
            Sets the source reference on Chart Studio Cloud for
            values .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Treemap

        new_trace = Treemap(
            branchvalues=branchvalues,
            count=count,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            labels=labels,
            labelssrc=labelssrc,
            level=level,
            marker=marker,
            maxdepth=maxdepth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            parents=parents,
            parentssrc=parentssrc,
            pathbar=pathbar,
            sort=sort,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            tiling=tiling,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_violin(
        self,
        alignmentgroup=None,
        bandwidth=None,
        box=None,
        customdata=None,
        customdatasrc=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        jitter=None,
        legendgroup=None,
        line=None,
        marker=None,
        meanline=None,
        meta=None,
        metasrc=None,
        name=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        pointpos=None,
        points=None,
        scalegroup=None,
        scalemode=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        side=None,
        span=None,
        spanmode=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Violin trace
        
        In vertical (horizontal) violin plots, statistics are computed
        using `y` (`x`) values. By supplying an `x` (`y`) array, one
        violin per distinct x (y) value is drawn If no `x` (`y`) list
        is provided, a single violin is drawn. That violin position is
        then positioned with with `name` or with `x0` (`y0`) if
        provided.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        bandwidth
            Sets the bandwidth used to compute the kernel density
            estimate. By default, the bandwidth is determined by
            Silverman's rule of thumb.
        box
            :class:`plotly.graph_objects.violin.Box` instance or
            dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.violin.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual violins or
            sample points or the kernel density estimate or any
            combination of them?
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        jitter
            Sets the amount of jitter in the sample points drawn.
            If 0, the sample points align along the distribution
            axis. If 1, the sample points are drawn in a random
            jitter of width equal to the width of the violins.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            :class:`plotly.graph_objects.violin.Line` instance or
            dict with compatible properties
        marker
            :class:`plotly.graph_objects.violin.Marker` instance or
            dict with compatible properties
        meanline
            :class:`plotly.graph_objects.violin.Meanline` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover. For violin traces, the name
            will also be used for the position coordinate, if `x`
            and `x0` (`y` and `y0` if horizontal) are missing and
            the position axis is categorical. Note that the trace
            name is also used as a default value for attribute
            `scalegroup` (please see its description for details).
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the violin(s). If "v" ("h"),
            the distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the violins. If 0, the sample points are places over
            the center of the violins. Positive (negative) values
            correspond to positions to the right (left) for
            vertical violins and above (below) for horizontal
            violins.
        points
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the violins are shown with no sample
            points. Defaults to "suspectedoutliers" when
            `marker.outliercolor` or `marker.line.outliercolor` is
            set, otherwise defaults to "outliers".
        scalegroup
            If there are multiple violins that should be sized
            according to to some metric (see `scalemode`), link
            them by providing a non-empty group id here shared by
            every trace in the same group. If a violin's `width` is
            undefined, `scalegroup` will default to the trace's
            name. In this case, violins with the same names will be
            linked together
        scalemode
            Sets the metric by which the width of each violin is
            determined."width" means each violin has the same (max)
            width*count* means the violins are scaled by the number
            of sample points makingup each violin.
        selected
            :class:`plotly.graph_objects.violin.Selected` instance
            or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        side
            Determines on which side of the position value the
            density function making up one half of a violin is
            plotted. Useful when comparing two violin traces under
            "overlay" mode, where one trace has `side` set to
            "positive" and the other to "negative".
        span
            Sets the span in data space for which the density
            function will be computed. Has an effect only when
            `spanmode` is set to "manual".
        spanmode
            Sets the method by which the span in data space where
            the density function will be computed. "soft" means the
            span goes from the sample's minimum value minus two
            bandwidths to the sample's maximum value plus two
            bandwidths. "hard" means the span goes from the
            sample's minimum to its maximum value. For custom span
            settings, use mode "manual" and fill in the `span`
            attribute.
        stream
            :class:`plotly.graph_objects.violin.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with each sample
            value. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.violin.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the width of the violin in data coordinates. If 0
            (default value) the width is automatically selected
            based on the positions of other violin traces in the
            same subplot.
        x
            Sets the x sample data or coordinates. See overview for
            more info.
        x0
            Sets the x coordinate for single-box traces or the
            starting coordinate for multi-box traces set using
            q1/median/q3. See overview for more info.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y sample data or coordinates. See overview for
            more info.
        y0
            Sets the y coordinate for single-box traces or the
            starting coordinate for multi-box traces set using
            q1/median/q3. See overview for more info.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Violin

        new_trace = Violin(
            alignmentgroup=alignmentgroup,
            bandwidth=bandwidth,
            box=box,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            jitter=jitter,
            legendgroup=legendgroup,
            line=line,
            marker=marker,
            meanline=meanline,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            pointpos=pointpos,
            points=points,
            scalegroup=scalegroup,
            scalemode=scalemode,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            side=side,
            span=span,
            spanmode=spanmode,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_volume(
        self,
        autocolorscale=None,
        caps=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        isomax=None,
        isomin=None,
        legendgroup=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        opacityscale=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        slices=None,
        spaceframe=None,
        stream=None,
        surface=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        value=None,
        valuesrc=None,
        visible=None,
        x=None,
        xsrc=None,
        y=None,
        ysrc=None,
        z=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs
    ):
        """
        Add a new Volume trace
        
        Draws volume trace between iso-min and iso-max values with
        coordinates given by four 1-dimensional arrays containing the
        `value`, `x`, `y` and `z` of every vertex of a uniform or non-
        uniform 3-D grid. Horizontal or vertical slices, caps as well
        as spaceframe between iso-min and iso-max values could also be
        drawn using this trace.

        Parameters
        ----------
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        caps
            :class:`plotly.graph_objects.volume.Caps` instance or
            dict with compatible properties
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `value`) or the
            bounds set in `cmin` and `cmax`  Defaults to `false`
            when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `value` and if set, `cmin` must
            be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `value`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `value` and if set, `cmax` must
            be set as well.
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.volume.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        contour
            :class:`plotly.graph_objects.volume.Contour` instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.volume.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        isomax
            Sets the maximum boundary for iso-surface plot.
        isomin
            Sets the minimum boundary for iso-surface plot.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        lighting
            :class:`plotly.graph_objects.volume.Lighting` instance
            or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.volume.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        opacityscale
            Sets the opacityscale. The opacityscale must be an
            array containing arrays mapping a normalized value to
            an opacity value. At minimum, a mapping for the lowest
            (0) and highest (1) values are required. For example,
            `[[0, 1], [0.5, 0.2], [1, 1]]` means that higher/lower
            values would have higher opacity values and those in
            the middle would be more transparent Alternatively,
            `opacityscale` may be a palette name string of the
            following list: 'min', 'max', 'extremes' and 'uniform'.
            The default is 'uniform'.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        slices
            :class:`plotly.graph_objects.volume.Slices` instance or
            dict with compatible properties
        spaceframe
            :class:`plotly.graph_objects.volume.Spaceframe`
            instance or dict with compatible properties
        stream
            :class:`plotly.graph_objects.volume.Stream` instance or
            dict with compatible properties
        surface
            :class:`plotly.graph_objects.volume.Surface` instance
            or dict with compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        value
            Sets the 4th dimension (value) of the vertices.
        valuesrc
            Sets the source reference on Chart Studio Cloud for
            value .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices on X axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the Y coordinates of the vertices on Y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        z
            Sets the Z coordinates of the vertices on Z axis.
        zsrc
            Sets the source reference on Chart Studio Cloud for  z
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Volume

        new_trace = Volume(
            autocolorscale=autocolorscale,
            caps=caps,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            isomax=isomax,
            isomin=isomin,
            legendgroup=legendgroup,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            opacityscale=opacityscale,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            slices=slices,
            spaceframe=spaceframe,
            stream=stream,
            surface=surface,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            value=value,
            valuesrc=valuesrc,
            visible=visible,
            x=x,
            xsrc=xsrc,
            y=y,
            ysrc=ysrc,
            z=z,
            zsrc=zsrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_waterfall(
        self,
        alignmentgroup=None,
        base=None,
        cliponaxis=None,
        connector=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        insidetextanchor=None,
        insidetextfont=None,
        legendgroup=None,
        measure=None,
        measuresrc=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        offsetsrc=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        totals=None,
        uid=None,
        uirevision=None,
        visible=None,
        width=None,
        widthsrc=None,
        x=None,
        x0=None,
        xaxis=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Add a new Waterfall trace
        
        Draws waterfall trace which is useful graph to displays the
        contribution of various elements (either positive or negative)
        in a bar chart. The data visualized by the span of the bars is
        set in `y` if `orientation` is set th "v" (the default) and the
        labels are set in `x`. By setting `orientation` to "h", the
        roles are interchanged.

        Parameters
        ----------
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        base
            Sets where the bar base is drawn (in position axis
            units).
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        connector
            :class:`plotly.graph_objects.waterfall.Connector`
            instance or dict with compatible properties
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        decreasing
            :class:`plotly.graph_objects.waterfall.Decreasing`
            instance or dict with compatible properties
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            hoverinfo .
        hoverlabel
            :class:`plotly.graph_objects.waterfall.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. The variables
            available in `hovertemplate` are the ones emitted as
            event data described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available. variables `initial`, `delta` and
            `final`. Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            hovertemplate .
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        increasing
            :class:`plotly.graph_objects.waterfall.Increasing`
            instance or dict with compatible properties
        insidetextanchor
            Determines if texts are kept at center or start/end
            points in `textposition` "inside" mode.
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        measure
            An array containing types of values. By default the
            values are considered as 'relative'. However; it is
            possible to use 'total' to compute the sums. Also
            'absolute' could be applied to reset the computed total
            or to declare an initial value where needed.
        measuresrc
            Sets the source reference on Chart Studio Cloud for
            measure .
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        offsetsrc
            Sets the source reference on Chart Studio Cloud for
            offset .
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            :class:`plotly.graph_objects.waterfall.Stream` instance
            or dict with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textangle
            Sets the angle of the tick labels with respect to the
            bar. For example, a `tickangle` of -90 draws the tick
            labels vertically. With "auto" the texts may
            automatically be rotated to fit with the maximum size
            in bars.
        textfont
            Sets the font used for `text`.
        textinfo
            Determines which trace information appear on the graph.
            In the case of having multiple waterfalls, totals are
            computed separately (per trace).
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed), unless
            there is another bar stacked on this one, then the text
            gets pushed inside. "auto" tries to position `text`
            inside the bar, but if the bar is too small and no bar
            is stacked on this one the text is moved outside.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            textposition .
        textsrc
            Sets the source reference on Chart Studio Cloud for
            text .
        texttemplate
            Template string used for rendering the information text
            that appear on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}". https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format for
            details on the formatting syntax. Dates are formatted
            using d3-time-format's syntax %{variable|d3-time-
            format}, for example "Day: %{2019-01-01|%A}".
            https://github.com/d3/d3-time-format#locale_format for
            details on the date formatting syntax. Every attributes
            that can be specified per-point (the ones that are
            `arrayOk: true`) are available. variables `initial`,
            `delta`, `final` and `label`.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            texttemplate .
        totals
            :class:`plotly.graph_objects.waterfall.Totals` instance
            or dict with compatible properties
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        widthsrc
            Sets the source reference on Chart Studio Cloud for
            width .
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for  x
            .
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for  y
            .
        row : int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        col : int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import Waterfall

        new_trace = Waterfall(
            alignmentgroup=alignmentgroup,
            base=base,
            cliponaxis=cliponaxis,
            connector=connector,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legendgroup=legendgroup,
            measure=measure,
            measuresrc=measuresrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            offsetsrc=offsetsrc,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            totals=totals,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            **kwargs
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def select_coloraxes(self, selector=None, row=None, col=None):
        """
        Select coloraxis subplot objects from a particular subplot cell
        and/or coloraxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the coloraxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("coloraxis", selector, row, col)

    def for_each_coloraxis(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all coloraxis objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single coloraxis object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_coloraxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_coloraxes(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all coloraxis objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            coloraxis objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            coloraxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_coloraxes(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_geos(self, selector=None, row=None, col=None):
        """
        Select geo subplot objects from a particular subplot cell
        and/or geo subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the geo
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("geo", selector, row, col)

    def for_each_geo(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all geo objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single geo object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_geos(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_geos(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all geo objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            geo objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            geo object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_geos(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_mapboxes(self, selector=None, row=None, col=None):
        """
        Select mapbox subplot objects from a particular subplot cell
        and/or mapbox subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the mapbox
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("mapbox", selector, row, col)

    def for_each_mapbox(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all mapbox objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single mapbox object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_mapboxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_mapboxes(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all mapbox objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            mapbox objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            mapbox object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_mapboxes(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_polars(self, selector=None, row=None, col=None):
        """
        Select polar subplot objects from a particular subplot cell
        and/or polar subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the polar
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("polar", selector, row, col)

    def for_each_polar(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all polar objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single polar object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_polars(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_polars(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all polar objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            polar objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            polar object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_polars(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_scenes(self, selector=None, row=None, col=None):
        """
        Select scene subplot objects from a particular subplot cell
        and/or scene subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the scene
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("scene", selector, row, col)

    def for_each_scene(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all scene objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single scene object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_scenes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_scenes(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all scene objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            scene objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            scene object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_scenes(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_ternaries(self, selector=None, row=None, col=None):
        """
        Select ternary subplot objects from a particular subplot cell
        and/or ternary subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the ternary
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("ternary", selector, row, col)

    def for_each_ternary(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all ternary objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single ternary object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_ternaries(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_ternaries(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all ternary objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            ternary objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            ternary object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_ternaries(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_xaxes(self, selector=None, row=None, col=None):
        """
        Select xaxis subplot objects from a particular subplot cell
        and/or xaxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the xaxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("xaxis", selector, row, col)

    def for_each_xaxis(self, fn, selector=None, row=None, col=None):
        """
        Apply a function to all xaxis objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single xaxis object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_xaxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_xaxes(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ):
        """
        Perform a property update operation on all xaxis objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            xaxis objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            xaxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_xaxes(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_yaxes(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select yaxis subplot objects from a particular subplot cell
        and/or yaxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition. 
            
            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the yaxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            "yaxis", selector, row, col, secondary_y=secondary_y
        )

    def for_each_yaxis(self, fn, selector=None, row=None, col=None, secondary_y=None):
        """
        Apply a function to all yaxis objects that satisfy the
        specified selection criteria
        
        Parameters
        ----------
        fn:
            Function that inputs a single yaxis object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition. 
            
            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_yaxes(
            selector=selector, row=row, col=col, secondary_y=secondary_y
        ):
            fn(obj)

        return self

    def update_yaxes(
        self,
        patch=None,
        selector=None,
        overwrite=False,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Perform a property update operation on all yaxis objects
        that satisfy the specified selection criteria
        
        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            yaxis objects that satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition. 
            
            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected
            yaxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self.select_yaxes(
            selector=selector, row=row, col=col, secondary_y=secondary_y
        ):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_annotations(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select annotations from a particular subplot cell and/or annotations
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Annotations will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all annotations are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of annotations to select.
            To select annotations by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            annotation that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all annotations are selected.
        secondary_y: boolean or None (default None)
            * If True, only select annotations associated with the secondary
              y-axis of the subplot.
            * If False, only select annotations associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter annotations based on secondary
              y-axis.

            To select annotations by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the annotations that satisfy
            all of the specified selection criteria
        """
        return self._select_annotations_like(
            "annotations", selector=selector, row=row, col=col, secondary_y=secondary_y
        )

    def for_each_annotation(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Apply a function to all annotations that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single annotation object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all annotations are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of annotations to select.
            To select annotations by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            annotations that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all annotations are selected.
        secondary_y: boolean or None (default None)
            * If True, only select annotations associated with the secondary
              y-axis of the subplot.
            * If False, only select annotations associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter annotations based on secondary
              y-axis.

            To select annotations by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="annotations",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            fn(obj)

        return self

    def update_annotations(
        self, patch=None, selector=None, row=None, col=None, secondary_y=None, **kwargs
    ):
        """
        Perform a property update operation on all annotations that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all annotations that
            satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all annotations are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of annotations to select.
            To select annotations by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            annotation that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all annotations are selected.
        secondary_y: boolean or None (default None)
            * If True, only select annotations associated with the secondary
              y-axis of the subplot.
            * If False, only select annotations associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter annotations based on secondary
              y-axis.

            To select annotations by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected annotation. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="annotations",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            obj.update(patch, **kwargs)

        return self

    def add_annotation(
        self,
        arg=None,
        align=None,
        arrowcolor=None,
        arrowhead=None,
        arrowside=None,
        arrowsize=None,
        arrowwidth=None,
        ax=None,
        axref=None,
        ay=None,
        ayref=None,
        bgcolor=None,
        bordercolor=None,
        borderpad=None,
        borderwidth=None,
        captureevents=None,
        clicktoshow=None,
        font=None,
        height=None,
        hoverlabel=None,
        hovertext=None,
        name=None,
        opacity=None,
        showarrow=None,
        standoff=None,
        startarrowhead=None,
        startarrowsize=None,
        startstandoff=None,
        templateitemname=None,
        text=None,
        textangle=None,
        valign=None,
        visible=None,
        width=None,
        x=None,
        xanchor=None,
        xclick=None,
        xref=None,
        xshift=None,
        y=None,
        yanchor=None,
        yclick=None,
        yref=None,
        yshift=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Create and add a new annotation to the figure's layout
        
        Parameters
        ----------
        arg
            instance of Annotation or dict with compatible
            properties
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans two or more
            lines (i.e. `text` contains one or more <br> HTML tags)
            or if an explicit width is set to override the text
            width.
        arrowcolor
            Sets the color of the annotation arrow.
        arrowhead
            Sets the end annotation arrow head style.
        arrowside
            Sets the annotation arrow head position.
        arrowsize
            Sets the size of the end annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        arrowwidth
            Sets the width (in px) of annotation arrow line.
        ax
            Sets the x component of the arrow tail about the arrow
            head. If `axref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from right
            to left (left to right). If `axref` is an axis, this is
            an absolute value on that axis, like `x`, NOT a
            relative value.
        axref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ax` is a relative
            offset in pixels  from `x`. If set to an x axis id
            (e.g. "x" or "x2"), `ax` is  specified in the same
            terms as that axis. This is useful  for trendline
            annotations which should continue to indicate  the
            correct trend when zoomed.
        ay
            Sets the y component of the arrow tail about the arrow
            head. If `ayref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from bottom
            to top (top to bottom). If `ayref` is an axis, this is
            an absolute value on that axis, like `y`, NOT a
            relative value.
        ayref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ay` is a relative
            offset in pixels  from `y`. If set to a y axis id (e.g.
            "y" or "y2"), `ay` is  specified in the same terms as
            that axis. This is useful  for trendline annotations
            which should continue to indicate  the correct trend
            when zoomed.
        bgcolor
            Sets the background color of the annotation.
        bordercolor
            Sets the color of the border enclosing the annotation
            `text`.
        borderpad
            Sets the padding (in px) between the `text` and the
            enclosing border.
        borderwidth
            Sets the width (in px) of the border enclosing the
            annotation `text`.
        captureevents
            Determines whether the annotation text box captures
            mouse move and click events, or allows those events to
            pass through to data points in the plot that may be
            behind the annotation. By default `captureevents` is
            False unless `hovertext` is provided. If you use the
            event `plotly_clickannotation` without `hovertext` you
            must explicitly enable `captureevents`.
        clicktoshow
            Makes this annotation respond to clicks on the plot. If
            you click a data point that exactly matches the `x` and
            `y` values of this annotation, and it is hidden
            (visible: false), it will appear. In "onoff" mode, you
            must click the same point again to make it disappear,
            so if you click multiple points, you can show multiple
            annotations. In "onout" mode, a click anywhere else in
            the plot (on another data point or not) will hide this
            annotation. If you need to show/hide this annotation in
            response to different `x` or `y` values, you can set
            `xclick` and/or `yclick`. This is useful for example to
            label the side of a bar. To label markers though,
            `standoff` is preferred over `xclick` and `yclick`.
        font
            Sets the annotation text font.
        height
            Sets an explicit height for the text box. null
            (default) lets the text set the box height. Taller text
            will be clipped.
        hoverlabel
            :class:`plotly.graph_objects.layout.annotation.Hoverlab
            el` instance or dict with compatible properties
        hovertext
            Sets text to appear when hovering over this annotation.
            If omitted or blank, no hover label will appear.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the annotation (text + arrow).
        showarrow
            Determines whether or not the annotation is drawn with
            an arrow. If True, `text` is placed near the arrow's
            tail. If False, `text` lines up with the `x` and `y`
            provided.
        standoff
            Sets a distance, in pixels, to move the end arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        startarrowhead
            Sets the start annotation arrow head style.
        startarrowsize
            Sets the size of the start annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        startstandoff
            Sets a distance, in pixels, to move the start arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        text
            Sets the text associated with this annotation. Plotly
            uses a subset of HTML tags to do things like newline
            (<br>), bold (<b></b>), italics (<i></i>), hyperlinks
            (<a href='...'></a>). Tags <em>, <sup>, <sub> <span>
            are also supported.
        textangle
            Sets the angle at which the `text` is drawn with
            respect to the horizontal.
        valign
            Sets the vertical alignment of the `text` within the
            box. Has an effect only if an explicit height is set to
            override the text height.
        visible
            Determines whether or not this annotation is visible.
        width
            Sets an explicit width for the text box. null (default)
            lets the text set the box width. Wider text will be
            clipped. There is no automatic wrapping; use <br> to
            start a new line.
        x
            Sets the annotation's x position. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        xanchor
            Sets the text box's horizontal position anchor This
            anchor binds the `x` position to the "left", "center"
            or "right" of the annotation. For example, if `x` is
            set to 1, `xref` to "paper" and `xanchor` to "right"
            then the right-most portion of the annotation lines up
            with the right-most edge of the plotting area. If
            "auto", the anchor is equivalent to "center" for data-
            referenced annotations or if there is an arrow, whereas
            for paper-referenced with no arrow, the anchor picked
            corresponds to the closest side.
        xclick
            Toggle this annotation when clicking a data point whose
            `x` value is `xclick` rather than the annotation's `x`
            value.
        xref
            Sets the annotation's x coordinate axis. If set to an x
            axis id (e.g. "x" or "x2"), the `x` position refers to
            an x coordinate If set to "paper", the `x` position
            refers to the distance from the left side of the
            plotting area in normalized coordinates where 0 (1)
            corresponds to the left (right) side.
        xshift
            Shifts the position of the whole annotation and arrow
            to the right (positive) or left (negative) by this many
            pixels.
        y
            Sets the annotation's y position. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        yanchor
            Sets the text box's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the annotation. For example, if `y` is set
            to 1, `yref` to "paper" and `yanchor` to "top" then the
            top-most portion of the annotation lines up with the
            top-most edge of the plotting area. If "auto", the
            anchor is equivalent to "middle" for data-referenced
            annotations or if there is an arrow, whereas for paper-
            referenced with no arrow, the anchor picked corresponds
            to the closest side.
        yclick
            Toggle this annotation when clicking a data point whose
            `y` value is `yclick` rather than the annotation's `y`
            value.
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. "y" or "y2"), the `y` position refers to
            an y coordinate If set to "paper", the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        yshift
            Shifts the position of the whole annotation and arrow
            up (positive) or down (negative) by this many pixels.
        row
            Subplot row for annotation
        col
            Subplot column for annotation
        secondary_y
            Whether to add annotation to secondary y-axis

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import layout as _layout

        new_obj = _layout.Annotation(
            arg,
            align=align,
            arrowcolor=arrowcolor,
            arrowhead=arrowhead,
            arrowside=arrowside,
            arrowsize=arrowsize,
            arrowwidth=arrowwidth,
            ax=ax,
            axref=axref,
            ay=ay,
            ayref=ayref,
            bgcolor=bgcolor,
            bordercolor=bordercolor,
            borderpad=borderpad,
            borderwidth=borderwidth,
            captureevents=captureevents,
            clicktoshow=clicktoshow,
            font=font,
            height=height,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            name=name,
            opacity=opacity,
            showarrow=showarrow,
            standoff=standoff,
            startarrowhead=startarrowhead,
            startarrowsize=startarrowsize,
            startstandoff=startstandoff,
            templateitemname=templateitemname,
            text=text,
            textangle=textangle,
            valign=valign,
            visible=visible,
            width=width,
            x=x,
            xanchor=xanchor,
            xclick=xclick,
            xref=xref,
            xshift=xshift,
            y=y,
            yanchor=yanchor,
            yclick=yclick,
            yref=yref,
            yshift=yshift,
            **kwargs
        )
        return self._add_annotation_like(
            "annotation",
            "annotations",
            new_obj,
            row=row,
            col=col,
            secondary_y=secondary_y,
        )

    def select_layout_images(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select images from a particular subplot cell and/or images
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Annotations will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all images are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of images to select.
            To select images by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            image that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all images are selected.
        secondary_y: boolean or None (default None)
            * If True, only select images associated with the secondary
              y-axis of the subplot.
            * If False, only select images associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter images based on secondary
              y-axis.

            To select images by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the images that satisfy
            all of the specified selection criteria
        """
        return self._select_annotations_like(
            "images", selector=selector, row=row, col=col, secondary_y=secondary_y
        )

    def for_each_layout_image(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Apply a function to all images that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single image object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all images are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of images to select.
            To select images by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            images that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all images are selected.
        secondary_y: boolean or None (default None)
            * If True, only select images associated with the secondary
              y-axis of the subplot.
            * If False, only select images associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter images based on secondary
              y-axis.

            To select images by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="images", selector=selector, row=row, col=col, secondary_y=secondary_y,
        ):
            fn(obj)

        return self

    def update_layout_images(
        self, patch=None, selector=None, row=None, col=None, secondary_y=None, **kwargs
    ):
        """
        Perform a property update operation on all images that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all images that
            satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all images are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of images to select.
            To select images by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            image that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all images are selected.
        secondary_y: boolean or None (default None)
            * If True, only select images associated with the secondary
              y-axis of the subplot.
            * If False, only select images associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter images based on secondary
              y-axis.

            To select images by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected image. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="images", selector=selector, row=row, col=col, secondary_y=secondary_y,
        ):
            obj.update(patch, **kwargs)

        return self

    def add_layout_image(
        self,
        arg=None,
        layer=None,
        name=None,
        opacity=None,
        sizex=None,
        sizey=None,
        sizing=None,
        source=None,
        templateitemname=None,
        visible=None,
        x=None,
        xanchor=None,
        xref=None,
        y=None,
        yanchor=None,
        yref=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Create and add a new image to the figure's layout
        
        Parameters
        ----------
        arg
            instance of Image or dict with compatible properties
        layer
            Specifies whether images are drawn below or above
            traces. When `xref` and `yref` are both set to `paper`,
            image is drawn below the entire plot area.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the image.
        sizex
            Sets the image container size horizontally. The image
            will be sized based on the `position` value. When
            `xref` is set to `paper`, units are sized relative to
            the plot width.
        sizey
            Sets the image container size vertically. The image
            will be sized based on the `position` value. When
            `yref` is set to `paper`, units are sized relative to
            the plot height.
        sizing
            Specifies which dimension of the image to constrain.
        source
            Specifies the URL of the image to be used. The URL must
            be accessible from the domain where the plot code is
            run, and can be either relative or absolute.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        visible
            Determines whether or not this image is visible.
        x
            Sets the image's x position. When `xref` is set to
            `paper`, units are sized relative to the plot height.
            See `xref` for more info
        xanchor
            Sets the anchor for the x position
        xref
            Sets the images's x coordinate axis. If set to a x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            data coordinate If set to "paper", the `x` position
            refers to the distance from the left of plot in
            normalized coordinates where 0 (1) corresponds to the
            left (right).
        y
            Sets the image's y position. When `yref` is set to
            `paper`, units are sized relative to the plot height.
            See `yref` for more info
        yanchor
            Sets the anchor for the y position.
        yref
            Sets the images's y coordinate axis. If set to a y axis
            id (e.g. "y" or "y2"), the `y` position refers to a y
            data coordinate. If set to "paper", the `y` position
            refers to the distance from the bottom of the plot in
            normalized coordinates where 0 (1) corresponds to the
            bottom (top).
        row
            Subplot row for image
        col
            Subplot column for image
        secondary_y
            Whether to add image to secondary y-axis

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import layout as _layout

        new_obj = _layout.Image(
            arg,
            layer=layer,
            name=name,
            opacity=opacity,
            sizex=sizex,
            sizey=sizey,
            sizing=sizing,
            source=source,
            templateitemname=templateitemname,
            visible=visible,
            x=x,
            xanchor=xanchor,
            xref=xref,
            y=y,
            yanchor=yanchor,
            yref=yref,
            **kwargs
        )
        return self._add_annotation_like(
            "image", "images", new_obj, row=row, col=col, secondary_y=secondary_y,
        )

    def select_shapes(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select shapes from a particular subplot cell and/or shapes
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Annotations will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all shapes are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of shapes to select.
            To select shapes by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            shape that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all shapes are selected.
        secondary_y: boolean or None (default None)
            * If True, only select shapes associated with the secondary
              y-axis of the subplot.
            * If False, only select shapes associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter shapes based on secondary
              y-axis.

            To select shapes by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the shapes that satisfy
            all of the specified selection criteria
        """
        return self._select_annotations_like(
            "shapes", selector=selector, row=row, col=col, secondary_y=secondary_y
        )

    def for_each_shape(self, fn, selector=None, row=None, col=None, secondary_y=None):
        """
        Apply a function to all shapes that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single shape object.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all shapes are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of shapes to select.
            To select shapes by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            shapes that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all shapes are selected.
        secondary_y: boolean or None (default None)
            * If True, only select shapes associated with the secondary
              y-axis of the subplot.
            * If False, only select shapes associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter shapes based on secondary
              y-axis.

            To select shapes by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="shapes", selector=selector, row=row, col=col, secondary_y=secondary_y,
        ):
            fn(obj)

        return self

    def update_shapes(
        self, patch=None, selector=None, row=None, col=None, secondary_y=None, **kwargs
    ):
        """
        Perform a property update operation on all shapes that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all shapes that
            satisfy the selection criteria.
        selector: dict or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all shapes are
            selected.
        row, col: int or None (default None)
            Subplot row and column index of shapes to select.
            To select shapes by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            shape that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all shapes are selected.
        secondary_y: boolean or None (default None)
            * If True, only select shapes associated with the secondary
              y-axis of the subplot.
            * If False, only select shapes associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter shapes based on secondary
              y-axis.

            To select shapes by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected shape. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="shapes", selector=selector, row=row, col=col, secondary_y=secondary_y,
        ):
            obj.update(patch, **kwargs)

        return self

    def add_shape(
        self,
        arg=None,
        editable=None,
        fillcolor=None,
        fillrule=None,
        layer=None,
        line=None,
        name=None,
        opacity=None,
        path=None,
        templateitemname=None,
        type=None,
        visible=None,
        x0=None,
        x1=None,
        xanchor=None,
        xref=None,
        xsizemode=None,
        y0=None,
        y1=None,
        yanchor=None,
        yref=None,
        ysizemode=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        """
        Create and add a new shape to the figure's layout
        
        Parameters
        ----------
        arg
            instance of Shape or dict with compatible properties
        editable
            Determines whether the shape could be activated for
            edit or not. Has no effect when the older editable
            shapes mode is enabled via `config.editable` or
            `config.edits.shapePosition`.
        fillcolor
            Sets the color filling the shape's interior. Only
            applies to closed shapes.
        fillrule
            Determines which regions of complex paths constitute
            the interior. For more info please visit
            https://developer.mozilla.org/en-
            US/docs/Web/SVG/Attribute/fill-rule
        layer
            Specifies whether shapes are drawn below or above
            traces.
        line
            :class:`plotly.graph_objects.layout.shape.Line`
            instance or dict with compatible properties
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the shape.
        path
            For `type` "path" - a valid SVG path with the pixel
            values replaced by data values in
            `xsizemode`/`ysizemode` being "scaled" and taken
            unmodified as pixels relative to `xanchor` and
            `yanchor` in case of "pixel" size mode. There are a few
            restrictions / quirks only absolute instructions, not
            relative. So the allowed segments are: M, L, H, V, Q,
            C, T, S, and Z arcs (A) are not allowed because radius
            rx and ry are relative. In the future we could consider
            supporting relative commands, but we would have to
            decide on how to handle date and log axes. Note that
            even as is, Q and C Bezier paths that are smooth on
            linear axes may not be smooth on log, and vice versa.
            no chained "polybezier" commands - specify the segment
            type for each one. On category axes, values are numbers
            scaled to the serial numbers of categories because
            using the categories themselves there would be no way
            to describe fractional positions On data axes: because
            space and T are both normal components of path strings,
            we can't use either to separate date from time parts.
            Therefore we'll use underscore for this purpose:
            2015-02-21_13:45:56.789
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Specifies the shape type to be drawn. If "line", a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect
            to the axes' sizing mode. If "circle", a circle is
            drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
            (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with
            respect to the axes' sizing mode. If "rect", a
            rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`),
            (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect to
            the axes' sizing mode. If "path", draw a custom SVG
            path using `path`. with respect to the axes' sizing
            mode.
        visible
            Determines whether or not this shape is visible.
        x0
            Sets the shape's starting x position. See `type` and
            `xsizemode` for more info.
        x1
            Sets the shape's end x position. See `type` and
            `xsizemode` for more info.
        xanchor
            Only relevant in conjunction with `xsizemode` set to
            "pixel". Specifies the anchor point on the x axis to
            which `x0`, `x1` and x coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `xsizemode` not
            set to "pixel".
        xref
            Sets the shape's x coordinate axis. If set to an x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            coordinate. If set to "paper", the `x` position refers
            to the distance from the left side of the plotting area
            in normalized coordinates where 0 (1) corresponds to
            the left (right) side. If the axis `type` is "log",
            then you must take the log of your desired range. If
            the axis `type` is "date", then you must convert the
            date to unix time in milliseconds.
        xsizemode
            Sets the shapes's sizing mode along the x axis. If set
            to "scaled", `x0`, `x1` and x coordinates within `path`
            refer to data values on the x axis or a fraction of the
            plot area's width (`xref` set to "paper"). If set to
            "pixel", `xanchor` specifies the x position in terms of
            data or plot fraction but `x0`, `x1` and x coordinates
            within `path` are pixels relative to `xanchor`. This
            way, the shape can have a fixed width while maintaining
            a position relative to data or plot fraction.
        y0
            Sets the shape's starting y position. See `type` and
            `ysizemode` for more info.
        y1
            Sets the shape's end y position. See `type` and
            `ysizemode` for more info.
        yanchor
            Only relevant in conjunction with `ysizemode` set to
            "pixel". Specifies the anchor point on the y axis to
            which `y0`, `y1` and y coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `ysizemode` not
            set to "pixel".
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. "y" or "y2"), the `y` position refers to
            an y coordinate If set to "paper", the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        ysizemode
            Sets the shapes's sizing mode along the y axis. If set
            to "scaled", `y0`, `y1` and y coordinates within `path`
            refer to data values on the y axis or a fraction of the
            plot area's height (`yref` set to "paper"). If set to
            "pixel", `yanchor` specifies the y position in terms of
            data or plot fraction but `y0`, `y1` and y coordinates
            within `path` are pixels relative to `yanchor`. This
            way, the shape can have a fixed height while
            maintaining a position relative to data or plot
            fraction.
        row
            Subplot row for shape
        col
            Subplot column for shape
        secondary_y
            Whether to add shape to secondary y-axis

        Returns
        -------
        Figure
        """
        from plotly.graph_objs import layout as _layout

        new_obj = _layout.Shape(
            arg,
            editable=editable,
            fillcolor=fillcolor,
            fillrule=fillrule,
            layer=layer,
            line=line,
            name=name,
            opacity=opacity,
            path=path,
            templateitemname=templateitemname,
            type=type,
            visible=visible,
            x0=x0,
            x1=x1,
            xanchor=xanchor,
            xref=xref,
            xsizemode=xsizemode,
            y0=y0,
            y1=y1,
            yanchor=yanchor,
            yref=yref,
            ysizemode=ysizemode,
            **kwargs
        )
        return self._add_annotation_like(
            "shape", "shapes", new_obj, row=row, col=col, secondary_y=secondary_y,
        )
