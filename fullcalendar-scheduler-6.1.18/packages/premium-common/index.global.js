/*!
FullCalendar Premium Common v6.1.18
Docs & License: https://fullcalendar.io/docs/premium
(c) 2024 Adam Shaw
*/
FullCalendar.PremiumCommon = (function (exports, core, internal, preact) {
    'use strict';

    // ...existing code...

    const OPTION_REFINERS = {
        schedulerLicenseKey: String,
    };

    var plugin = core.createPlugin({
        name: '@fullcalendar/premium-common',
        premiumReleaseDate: '2025-06-30',
        optionRefiners: OPTION_REFINERS,
        viewContainerAppends: [],
    });

    core.globalPlugins.push(plugin);

    exports["default"] = plugin;

    Object.defineProperty(exports, '__esModule', { value: true });

    return exports;

})({}, FullCalendar, FullCalendar.Internal, FullCalendar.Preact);
