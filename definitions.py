"""Themes color definitions."""

from build import ColorSplit

# Colors

colorNone = ColorSplit("#18181b").set_alpha(0)
colorWhite = ColorSplit("#fafafa")
colorBlack = ColorSplit("#18181b")
colorGrey = ColorSplit("#a1a1aa", "#52525b")
colorGreyStrong = ColorSplit("#52525b", "#71717a")
colorGreyLight = ColorSplit("#e4e4e7", "#3f3f46")
colorGreyOnBlack = ColorSplit("#52525b", colorGrey)

colorPurple = ColorSplit("#9333ea")
colorBlue = ColorSplit("#2563eb")
colorCyan = ColorSplit("#0891b2")
colorGreen = ColorSplit("#059669")
colorYellow = ColorSplit("#ca8a04")
colorOrange = ColorSplit("#ea580c")
colorRed = ColorSplit("#dc2626")

colorMain = ColorSplit(colorWhite, colorBlack)
colorMainNegative = ColorSplit(colorBlack, colorWhite)
colorMainContrast = ColorSplit("#f4f4f5", "#52525b")
colorMainContrastTransparent = ColorSplit("#5b21b6", "#4c1d95").set_alpha(0.1)

colorPrimary = ColorSplit(colorBlue, colorPurple)
colorPrimaryNegative = colorWhite
colorPrimaryHighlight = ColorSplit("#6366f1", colorPrimary).set_alpha(0.15, 0.25)
colorPrimaryHighlightStrong = colorPrimaryHighlight.with_alpha(0.3, 0.5)
colorPrimaryHighlightLight = colorPrimaryHighlight.with_alpha(0.05, 0.08)

colorAdded = colorGreen
colorAddedHighlight = colorAdded.with_alpha(0.1, 0.2)
colorDeleted = colorRed
colorDeletedHighlight = colorDeleted.with_alpha(0.1, 0.2)

colorError = colorRed
colorWarning = colorOrange

colorFind = colorGreen.with_alpha(0.8)
colorFindHighlight = colorFind.with_alpha(0.4)

colorStackFocused = colorOrange.with_alpha(0.6)
colorStack = colorOrange.with_alpha(0.3)

colorBorder = colorGreyLight

# Theme definitions

definitions = {
    "colors": {
        "activityBar.background": colorMain,
        "activityBar.border": colorNone,
        "activityBar.foreground": colorGrey,
        "activityBarBadge.background": colorMainNegative,
        "activityBarBadge.foreground": colorMain,
        "badge.background": colorMainNegative,
        "badge.foreground": colorMain,
        "button.background": colorPrimary,
        "button.foreground": colorPrimaryNegative,
        "contrastBorder": colorNone,
        "debugToolBar.background": colorMainContrast,
        "diffEditor.insertedTextBackground": colorAddedHighlight,
        "diffEditor.removedTextBackground": colorDeletedHighlight,
        "dropdown.background": colorMainContrast,
        "dropdown.border": colorBorder,
        "dropdown.foreground": colorMainNegative,
        "editor.background": colorMain,
        "editor.findMatchBackground": colorFind,
        "editor.findMatchHighlightBackground": colorFindHighlight,
        "editor.focusedStackFrameHighlightBackground": colorStackFocused,
        "editor.foreground": colorMainNegative,
        "editor.lineHighlightBackground": colorPrimaryHighlightLight,
        "editor.lineHighlightBorder": colorNone,
        "editor.selectionBackground": colorPrimaryHighlightStrong,
        "editor.selectionForeground": colorMain,
        "editor.selectionHighlightBorder": ColorSplit(colorNone, colorPrimaryHighlight),
        "editor.stackFrameHighlightBackground": colorStack,
        "editor.wordHighlightBackground": colorPrimaryHighlight,
        "editor.wordHighlightStrongBackground": colorPrimaryHighlightStrong,
        "editorBracketMatch.background": colorPrimaryHighlightStrong,
        "editorBracketMatch.border": colorNone,
        "editorCursor.foreground": colorPrimary,
        "editorError.foreground": colorError,
        "editorGroup.border": colorMainContrast,
        "editorGroupHeader.tabsBackground": colorMain,
        "editorGroupHeader.tabsBorder": colorNone,
        "editorGutter.addedBackground": colorAdded,
        "editorGutter.deletedBackground": colorDeleted,
        "editorGutter.modifiedBackground": colorMainNegative,
        "editorIndentGuide.background": colorMainContrast,
        "editorLineNumber.activeForeground": colorGrey,
        "editorLineNumber.foreground": ColorSplit("#ebf0f5", colorGreyLight),
        "editorLink.activeForeground": colorPrimary,
        "editorOverviewRuler.addedForeground": colorNone,
        "editorOverviewRuler.border": colorNone,
        "editorOverviewRuler.bracketMatchForeground": colorPrimaryHighlightStrong,
        "editorOverviewRuler.errorForeground": colorError,
        "editorOverviewRuler.findMatchForeground": colorFind,
        "editorOverviewRuler.modifiedForeground": colorMainNegative,
        "editorOverviewRuler.selectionHighlightForeground": colorPrimaryHighlightStrong,
        "editorOverviewRuler.warningForeground": colorWarning,
        "editorOverviewRuler.wordHighlightForeground": colorPrimaryHighlight,
        "editorOverviewRuler.wordHighlightStrongForeground": colorPrimaryHighlightStrong,
        "editorRuler.foreground": colorMainContrast,
        "editorSuggestWidget.foreground": colorMainNegative,
        "editorSuggestWidget.highlightForeground": colorFindHighlight,
        "editorWarning.foreground": colorWarning,
        "editorWidget.background": colorMainContrast,
        "editorWidget.border": colorBorder,
        "errorForeground": colorError,
        "extensionButton.prominentBackground": colorPrimary,
        "extensionButton.prominentForeground": colorPrimaryNegative,
        "extensionButton.prominentHoverBackground": colorPrimary,
        "focusBorder": colorBorder,
        "foreground": colorMainNegative,
        "gitDecoration.ignoredResourceForeground": colorGrey,
        "gitDecoration.modifiedResourceForeground": colorMainNegative,
        "gitDecoration.untrackedResourceForeground": colorMainNegative,
        "input.background": colorMainContrast,
        "input.border": colorBorder,
        "input.foreground": colorMainNegative,
        "input.placeholderForeground": colorGrey,
        "list.activeSelectionBackground": colorMainNegative,
        "list.activeSelectionForeground": colorMain,
        "list.dropBackground": colorPrimaryHighlightStrong,
        "list.focusBackground": colorPrimaryHighlight,
        "list.focusForeground": colorMainNegative,
        "list.highlightForeground": colorMainNegative,
        "list.hoverBackground": colorMainContrast,
        "list.inactiveSelectionBackground": colorMainContrast,
        "list.inactiveSelectionForeground": colorMainNegative,
        "panel.background": colorMainContrast,
        "panel.border": colorNone,
        "panelTitle.activeBorder": colorGrey,
        "peekView.border": colorMainNegative,
        "peekViewEditor.background": colorNone,
        "peekViewEditor.matchHighlightBackground": colorFind,
        "peekViewResult.background": colorNone,
        "peekViewResult.fileForeground": colorGreyStrong,
        "peekViewResult.lineForeground": colorGreyStrong,
        "peekViewResult.matchHighlightBackground": colorFind,
        "peekViewResult.selectionBackground": colorMainNegative,
        "peekViewResult.selectionForeground": colorMain,
        "peekViewTitle.background": colorNone,
        "peekViewTitleDescription.foreground": colorGrey,
        "peekViewTitleLabel.foreground": colorMainNegative,
        "progressBar.background": colorPrimary,
        "scrollbar.shadow": colorNone,
        "scrollbarSlider.background": colorMainContrastTransparent,
        "scrollbarSlider.hoverBackground": colorMainNegative,
        "sideBar.background": colorMain,
        "sideBar.foreground": colorGreyStrong,
        "sideBarSectionHeader.background": colorMainContrast,
        "sideBarSectionHeader.foreground": colorGreyStrong,
        "sideBarTitle.foreground": colorGrey,
        "statusBar.background": colorBlack,
        "statusBar.debuggingBackground": colorOrange,
        "statusBar.debuggingForeground": colorBlack,
        "statusBar.foreground": colorGreyOnBlack,
        "statusBar.noFolderBackground": colorBlack,
        "tab.activeBackground": colorGreyStrong,
        "tab.activeForeground": colorMain,
        "tab.activeModifiedBorder": colorNone,
        "tab.border": colorNone,
        "tab.inactiveBackground": colorNone,
        "tab.inactiveForeground": colorGreyStrong,
        "tab.inactiveModifiedBorder": colorMainNegative,
        "terminal.ansiBlack": colorMainNegative,
        "terminal.ansiBlue": colorBlue,
        "terminal.ansiBrightBlack": colorMainNegative,
        "terminal.ansiBrightBlue": colorBlue,
        "terminal.ansiBrightCyan": colorCyan,
        "terminal.ansiBrightGreen": colorGreen,
        "terminal.ansiBrightMagenta": colorPurple,
        "terminal.ansiBrightRed": colorRed,
        "terminal.ansiBrightWhite": colorWhite,
        "terminal.ansiBrightYellow": colorYellow,
        "terminal.ansiCyan": colorCyan,
        "terminal.ansiGreen": colorGreen,
        "terminal.ansiMagenta": colorPurple,
        "terminal.ansiRed": colorRed,
        "terminal.ansiWhite": colorWhite,
        "terminal.ansiYellow": colorYellow,
        "terminal.foreground": colorMainNegative,
        "terminal.selectionBackground": colorPrimaryHighlightStrong,
        "terminalCursor.foreground": colorPrimary,
        "textLink.activeForeground": colorPrimary,
        "textLink.foreground": colorPrimary,
        "titleBar.activeBackground": colorMain,
        "titleBar.activeForeground": colorGreyStrong,
        "titleBar.inactiveBackground": colorMain,
        "titleBar.inactiveForeground": colorGrey,
        "welcomePage.buttonBackground": colorMainContrast,
        "welcomePage.buttonHoverBackground": colorPrimaryHighlight,
        "widget.shadow": colorNone,
    },
    "tokenColors": [
        {
            "scope": ["comment", "string.quoted.docstring"],
            "settings": {"foreground": colorGrey},
        },
        {"scope": ["string"], "settings": {"foreground": colorGreyStrong}},
        {
            "scope": ["punctuation.definition.string", "storage.type.string.python"],
            "settings": {"foreground": colorMainNegative},
        },
        {
            "scope": [
                "beginning.punctuation",
                "entity.name.section.group-title",
                "entity.name.tag",
                "entity.other.attribute-name.class",
                "entity.other.attribute-name.id",
                "keyword.const",
                "keyword.control",
                "keyword.function",
                "keyword.import",
                "keyword.operator.assignment",
                "keyword.operator.comparison",
                "keyword.operator.decrement",
                "keyword.operator.expression",
                "keyword.operator.increment",
                "keyword.operator.increment-decrement",
                "keyword.operator.logical",
                "keyword.operator.misc",
                "keyword.operator.new",
                "keyword.operator.other",
                "keyword.operator.ternary",
                "keyword.other.fn",
                "keyword.other.rust",
                "keyword.other.special-method",
                "keyword.other.where",
                "keyword.package",
                "keyword.type",
                "keyword.var",
                "markup.heading",
                "meta.tag.sgml.doctype.html",
                "punctuation.separator.key-value",
                "storage.modifier",
                "storage.type.class",
                "storage.type.enum",
                "storage.type.function",
                "storage.type.import",
                "storage.type.interface",
                "storage.type.js",
                "storage.type.namespace",
                "storage.type.property",
                "storage.type.rust",
                "storage.type.string.python",
                "storage.type.ts",
                "storage.type.tsx",
                "storage.type.type",
                "support.type.object.module",
            ],
            "settings": {"fontStyle": "bold"},
        },
    ],
}
