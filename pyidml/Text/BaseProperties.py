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

valid_properties = ['appliedCharacterStyle', 'appliedConditions', 'appliedLanguage', 'appliedParagraphStyle',
                    'autoLeading', 'autoTcy', 'baselineShift', 'bulletsAlignment', 'bulletsAndNumberingListType',
                    'bulletsTextAfter', 'capitalization', 'characterAlignment', 'characterDirection',
                    'characterRotation', 'composer', 'desiredGlyphScaling', 'desiredLetterSpacing',
                    'desiredWordSpacing', 'diacriticPosition', 'digitsType', 'dropCapCharacters', 'dropCapLines',
                    'dropCapDetail', 'endJoin', 'fillColor', 'fillTint', 'firstLineIndent', 'fontStyle', 'glyphForm',
                    'gotoNextX', 'gradientFillAngle', 'gradientFillLength', 'gradientFillStart', 'gradientStrokeAngle',
                    'gradientStrokeLength', 'gradientStrokeStart', 'gridAlignment', 'horizontalScale', 'hyphenWeight',
                    'hyphenateAfterFirst', 'hyphenateBeforeLast', 'hyphenateLadderLimit', 'hyphenateWordsLongerThan',
                    'hyphenationZone', 'justification', 'keepFirstLines', 'keepLastLines', 'keepWithNext',
                    'kerningMethod', 'kerningValue', 'keyboardDirection', 'lastLineIndent', 'leadingModel',
                    'leftIndent', 'maximumGlyphScaling', 'maximumLetterSpacing', 'maximumWordSpacing',
                    'minimumGlyphScaling', 'minimumLetterSpacing', 'minimumWordSpacing', 'miterLimit',
                    'numberingAlignment', 'numberingExpression', 'numberingLevel', 'numberingStartAt', 'otfFigureStyle',
                    'otfStylisticSets', 'pageNumberType', 'paragraphDirection', 'paragraphJustification', 'pointSize',
                    'position', 'positionalForm', 'rightIndent', 'ruleAboveGapTint', 'ruleAboveLeftIndent',
                    'ruleAboveLineWeight', 'ruleAboveOffset', 'ruleAboveRightIndent', 'ruleAboveTint', 'ruleAboveWidth',
                    'ruleBelowGapTint', 'ruleBelowLeftIndent', 'ruleBelowLineWeight', 'ruleBelowOffset',
                    'ruleBelowRightIndent', 'ruleBelowTint', 'ruleBelowWidth', 'singleWordJustification', 'skew',
                    'spaceAfter', 'spaceBefore', 'spanColumnInsideGutter', 'spanColumnOutsideGutter', 'spanColumnType',
                    'spanSplitColumnCount', 'startParagraph', 'strikeThroughGapTint', 'strikeThroughOffset',
                    'strikeThroughTint', 'strikeThroughWeight', 'strokeAlignment', 'strokeColor', 'strokeTint',
                    'strokeWeight', 'tracking', 'tsume', 'underlineGapTint', 'underlineOffset', 'underlineTint',
                    'underlineWeight', 'verticalScale', 'xOffsetDiacritic', 'yOffSetDiacritic', 'allGrepStyles',
                    'allLineStyles', 'allNestedStyles', 'appliedFont', 'appliedNumberingList', 'balanceRaggedLines',
                    'bulletChar', 'bulletsCharacterStyle', 'bulletsFont', 'bulletsFontStyle', 'customGlyph', 'leading',
                    'numberingCharacterStyle', 'numberingFormat', 'numberingRestartPolicies', 'openTypeFeatures',
                    'ruleAboveColor', 'ruleAboveGapColor', 'ruleAboveType', 'ruleBelowColor', 'ruleBelowGapColor',
                    'ruleBelowType', 'strikeThroughColor', 'strikeThroughGapColor', 'strikeThroughType', 'tabList',
                    'underlineColor', 'underlineGapColor', 'underlineType', 'autoTcyIncludeRoman',
                    'gridAlignFirstLineOnly', 'hyphenateAcrossColumns', 'hyphenateCapitalizedWords',
                    'hyphenateLastWord', 'hyphenation', 'ignoreEdgeAlignment', 'keepAllLinesTogether',
                    'keepLinesTogether', 'keepRuleAboveInFrame', 'keepWithPrevious', 'ligatures', 'noBreak',
                    'numberingApplyRestartPolicy', 'numberingContinue', 'otfContextualAlternative',
                    'otfDiscretionaryLigature', 'otfFraction', 'otfHVKana', 'otfHistorical',
                    'otfJustificationAlternate', 'otfLocale', 'otfMark', 'otfOrdinal', 'otfOverlapSwash',
                    'otfProportionalMetrics', 'otfRomanItalics', 'otfSlashedZero', 'otfStretchedAlternate',
                    'otfStylisticAlternate', 'otfSwash', 'otfTitling', 'overprintFill', 'overprintStroke', 'rensuuji',
                    'rotateSingleByteCharacters', 'ruleAbove', 'ruleAboveGapOverprint', 'ruleAboveOverprint',
                    'ruleBelow', 'ruleBelowGapOverprint', 'ruleBelowOverprint', 'scaleAffectsLineHeight',
                    'strikeThroughGapOverprint', 'strikeThroughOverprint', 'strikeThru', 'treatIdeographicSpaceAsSpace',
                    'underline', 'underlineGapOverprint', 'underlineOverprint']
