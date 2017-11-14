from weakref import WeakKeyDictionary


class CTBoolean(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, None)

    def __set__(self, instance, value):
        if value is not None:
            if isinstance(value, bool):
                self._values[instance] = value
            else:
                raise TypeError("Property must be a bool value or None.")
        else:
            self._values[instance] = None


class CTString(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, None)

    def __set__(self, instance, value):
        if value is not None:
            if isinstance(value, str):
                self._values[instance] = value
            else:
                raise TypeError("Property must be a string or None.")
        else:
            self._values[instance] = None


class CommonText(object):
    def __init__(self):
        self.appliedCharacterStyle = None
        self.appliedConditions = None
        self.appliedLanguage = None
        self.appliedParagraphStyle = None
        self.autoLeading = None
        self.autoTcy = None
        self.baselineShift = None
        self.bulletsAlignment = None
        self.bulletsAndNumberingListType = None
        self.bulletsTextAfter = None
        self.capitalization = None
        self.characterAlignment = None
        self.characterDirection = None
        self.characterRotation = None
        self.composer = None
        self.desiredGlyphScaling = None
        self.desiredLetterSpacing = None
        self.desiredWordSpacing = None
        self.diacriticPosition = None
        self.digitsType = None
        self.dropCapCharacters = None
        self.dropCapLines = None
        self.dropCapDetail = None
        self.endJoin = None
        self.fillColor = None
        self.fillTint = None
        self.firstLineIndent = None
        self.fontStyle = None
        self.glyphForm = None
        self.gotoNextX = None
        self.gradientFillAngle = None
        self.gradientFillLength = None
        self.gradientFillStart = None
        self.gradientStrokeAngle = None
        self.gradientStrokeLength = None
        self.gradientStrokeStart = None
        self.gridAlignment = None
        self.horizontalScale = None
        self.hyphenWeight = None
        self.hyphenateAfterFirst = None
        self.hyphenateBeforeLast = None
        self.hyphenateLadderLimit = None
        self.hyphenateWordsLongerThan = None
        self.hyphenationZone = None
        self.justification = None
        self.keepFirstLines = None
        self.keepLastLines = None
        self.keepWithNext = None
        self.kerningMethod = None
        self.kerningValue = None
        self.keyboardDirection = None
        self.lastLineIndent = None
        self.leadingModel = None
        self.leftIndent = None
        self.maximumGlyphScaling = None
        self.maximumLetterSpacing = None
        self.maximumWordSpacing = None
        self.minimumGlyphScaling = None
        self.minimumLetterSpacing = None
        self.minimumWordSpacing = None
        self.miterLimit = None
        self.numberingAlignment = None
        self.numberingExpression = None
        self.numberingLevel = None
        self.numberingStartAt = None
        self.otfFigureStyle = None
        self.otfStylisticSets = None
        self.pageNumberType = None
        self.paragraphDirection = None
        self.paragraphJustification = None
        self.pointSize = None
        self.position = None
        self.positionalForm = None
        self.rightIndent = None
        self.ruleAboveGapTint = None
        self.ruleAboveLeftIndent = None
        self.ruleAboveLineWeight = None
        self.ruleAboveOffset = None
        self.ruleAboveRightIndent = None
        self.ruleAboveTint = None
        self.ruleAboveWidth = None
        self.ruleBelowGapTint = None
        self.ruleBelowLeftIndent = None
        self.ruleBelowLineWeight = None
        self.ruleBelowOffset = None
        self.ruleBelowRightIndent = None
        self.ruleBelowTint = None
        self.ruleBelowWidth = None
        self.singleWordJustification = None
        self.skew = None
        self.spaceAfter = None
        self.spaceBefore = None
        self.spanColumnInsideGutter = None
        self.spanColumnOutsideGutter = None
        self.spanColumnType = None
        self.spanSplitColumnCount = None
        self.startParagraph = None
        self.strikeThroughGapTint = None
        self.strikeThroughOffset = None
        self.strikeThroughTint = None
        self.strikeThroughWeight = None
        self.strokeAlignment = None
        self.strokeColor = None
        self.strokeTint = None
        self.strokeWeight = None
        self.tracking = None
        self.tsume = None
        self.underlineGapTint = None
        self.underlineOffset = None
        self.underlineTint = None
        self.underlineWeight = None
        self.verticalScale = None
        self.xOffsetDiacritic = None
        self.yOffSetDiacritic = None

        self.allGrepStyles = None
        self.allLineStyles = None
        self.allNestedStyles = None
        self.appliedFont = None
        self.appliedNumberingList = None
        self.balanceRaggedLines = None
        self.bulletChar = None
        self.bulletsCharacterStyle = None
        self.bulletsFont = None
        self.bulletsFontStyle = None
        self.customGlyph = None
        self.leading = None
        self.numberingCharacterStyle = None
        self.numberingFormat = None
        self.numberingRestartPolicies = None
        self.openTypeFeatures = None
        self.ruleAboveColor = None
        self.ruleAboveGapColor = None
        self.ruleAboveType = None
        self.ruleBelowColor = None
        self.ruleBelowGapColor = None
        self.ruleBelowType = None
        self.strikeThroughColor = None
        self.strikeThroughGapColor = None
        self.strikeThroughType = None
        self.tabList = None
        self.underlineColor = None
        self.underlineGapColor = None
        self.underlineType = None


    # Boolean values
    autoTcyIncludeRoman = CTBoolean()
    gridAlignFirstLineOnly = CTBoolean()
    hyphenateAcrossColumns = CTBoolean()
    hyphenateCapitalizedWords = CTBoolean()
    hyphenateLastWord = CTBoolean()
    hyphenation = CTBoolean()
    ignoreEdgeAlignment = CTBoolean()
    keepAllLinesTogether = CTBoolean()
    keepLinesTogether = CTBoolean()
    keepRuleAboveInFrame = CTBoolean()
    keepWithPrevious = CTBoolean()
    ligatures = CTBoolean()
    noBreak = CTBoolean()
    numberingApplyRestartPolicy = CTBoolean()
    numberingContinue = CTBoolean()
    otfContextualAlternative = CTBoolean()
    otfDiscretionaryLigature = CTBoolean()
    otfFraction = CTBoolean()
    otfHVKana = CTBoolean()
    otfHistorical = CTBoolean()
    otfJustificationAlternate = CTBoolean()
    otfLocale = CTBoolean()
    otfMark = CTBoolean()
    otfOrdinal = CTBoolean()
    otfOverlapSwash = CTBoolean()
    otfProportionalMetrics = CTBoolean()
    otfRomanItalics = CTBoolean()
    otfSlashedZero = CTBoolean()
    otfStretchedAlternate = CTBoolean()
    otfStylisticAlternate = CTBoolean()
    otfSwash = CTBoolean()
    otfTitling = CTBoolean()
    overprintFill = CTBoolean()
    overprintStroke = CTBoolean()
    rensuuji = CTBoolean()
    rotateSingleByteCharacters = CTBoolean()
    ruleAbove = CTBoolean()
    ruleAboveGapOverprint = CTBoolean()
    ruleAboveOverprint = CTBoolean()
    ruleBelow = CTBoolean()
    ruleBelowGapOverprint = CTBoolean()
    ruleBelowOverprint = CTBoolean()
    scaleAffectsLineHeight = CTBoolean()
    strikeThroughGapOverprint = CTBoolean()
    strikeThroughOverprint = CTBoolean()
    strikeThru = CTBoolean()
    treatIdeographicSpaceAsSpace = CTBoolean()
    underline = CTBoolean()
    underlineGapOverprint = CTBoolean()
    underlineOverprint = CTBoolean()

    def set_word_spacing(self, *, minimum=None, desired=None, maximum=None):
        if minimum is not None:
            self.minimumWordSpacing = minimum
        if desired is not None:
            self.desiredWordSpacing = desired
        if maximum is not None:
            self.maximumWordSpacing = maximum

    def set_glyph_scaling(self, *, minimum=None, desired=None, maximum=None):
        if minimum is not None:
            self.minimumGlyphScaling = minimum
        if desired is not None:
            self.desiredGlyphScaling = desired
        if maximum is not None:
            self.maximumGlyphScaling = maximum

    def set_letter_spacing(self, *, minimum=None, desired=None, maximum=None):
        if minimum is not None:
            self.minimumLetterSpacing = minimum
        if desired is not None:
            self.desiredLetterSpacing = desired
        if maximum is not None:
            self.maximumLetterSpacing = maximum

    def set_justification(self, *, word=None, glyph=None, letter=None):
        """Accepts up to 3 sets of tuples containing 3 values to set justification settings"""
        if isinstance(word, tuple):
            self.set_word_spacing(word[0], word[1], word[2])
        if isinstance(glyph, tuple):
            self.set_glyph_scaling(glyph[0], glyph[1], glyph[2])
        if isinstance(letter, tuple):
            self.set_letter_spacing(letter[0], letter[1], letter[2])
