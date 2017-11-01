contents = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<?aid style="50" type="snippet" readerVersion="6.0" featureSet="257" product="8.0(370)" ?>
<?aid SnippetType="InCopyInterchange"?>
<Document DOMVersion="8.0" Self="d">
	<RootCharacterStyleGroup Self="u77">
		<CharacterStyle Self="CharacterStyle/$ID/[No character style]" Imported="false" Name="$ID/[No character style]" />
		<CharacterStyle Self="CharacterStyle/italic" Imported="false" KeyboardShortcut="0 0" Name="italic" FontStyle="Italic">
			<Properties>
				<BasedOn type="string">$ID/[No character style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
			</Properties>
		</CharacterStyle>
	</RootCharacterStyleGroup>
	<RootParagraphStyleGroup Self="u76">
		<ParagraphStyle Self="ParagraphStyle/$ID/NormalParagraphStyle" Name="$ID/NormalParagraphStyle" Imported="false" NextStyle="ParagraphStyle/$ID/NormalParagraphStyle" KeyboardShortcut="0 0">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/toc" Name="toc" Imported="false" NextStyle="ParagraphStyle/toc" KeyboardShortcut="0 0" PointSize="8" FirstLineIndent="0">
			<Properties>
				<BasedOn type="object">ParagraphStyle/p</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<Leading type="unit">13</Leading>
				<TabList type="list">
					<ListItem type="record">
						<Alignment type="enumeration">CenterAlign</Alignment>
						<AlignmentCharacter type="string">.</AlignmentCharacter>
						<Leader type="string">. </Leader>
						<Position type="unit">111</Position>
					</ListItem>
					<ListItem type="record">
						<Alignment type="enumeration">RightAlign</Alignment>
						<AlignmentCharacter type="string">.</AlignmentCharacter>
						<Leader type="string">. </Leader>
						<Position type="unit">216</Position>
					</ListItem>
				</TabList>
				<AllNestedStyles type="list">
					<ListItem type="record">
						<AppliedCharacterStyle type="object">CharacterStyle/$ID/[No character style]</AppliedCharacterStyle>
						<Delimiter type="enumeration">Tabs</Delimiter>
						<Repetition type="long">1</Repetition>
						<Inclusive type="boolean">true</Inclusive>
					</ListItem>
					<ListItem type="record">
						<AppliedCharacterStyle type="object">CharacterStyle/italic</AppliedCharacterStyle>
						<Delimiter type="enumeration">Tabs</Delimiter>
						<Repetition type="long">1</Repetition>
						<Inclusive type="boolean">true</Inclusive>
					</ListItem>
				</AllNestedStyles>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/p" Name="p" Imported="false" NextStyle="ParagraphStyle/p" KeyboardShortcut="0 0" PointSize="9" FirstLineIndent="12" HyphenateAfterFirst="3" HyphenateBeforeLast="3" HyphenateCapitalizedWords="false" HyphenateWordsLongerThan="6" KeepFirstLines="1" KeepLinesTogether="true" HyphenateLastWord="false" Justification="LeftJustified" HyphenateAcrossColumns="false">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<Leading type="unit">11</Leading>
				<AppliedFont type="string">Times</AppliedFont>
			</Properties>
		</ParagraphStyle>
	</RootParagraphStyleGroup>
	<TinDocumentDataObject>
		<Properties>
			<GaijiRefMaps><![CDATA[/////wAAAAAAAAAA]]></GaijiRefMaps>
		</Properties>
	</TinDocumentDataObject>
	<CrossReferenceFormat Self="u96" Name="Full Paragraph &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u96BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock1" BlockType="FullParagraphBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u97" Name="Full Paragraph" AppliedCharacterStyle="n">
		<BuildingBlock Self="u97BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u97BuildingBlock1" BlockType="FullParagraphBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u97BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u98" Name="Paragraph Text &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u98BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock1" BlockType="ParagraphTextBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u99" Name="Paragraph Text" AppliedCharacterStyle="n">
		<BuildingBlock Self="u99BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u99BuildingBlock1" BlockType="ParagraphTextBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u99BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9a" Name="Paragraph Number &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9aBuildingBlock0" BlockType="ParagraphNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9aBuildingBlock1" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText=" on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9aBuildingBlock2" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9b" Name="Paragraph Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9bBuildingBlock0" BlockType="ParagraphNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9c" Name="Text Anchor Name &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9cBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock1" BlockType="BookmarkNameBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9d" Name="Text Anchor Name" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9dBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9dBuildingBlock1" BlockType="BookmarkNameBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9dBuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9e" Name="Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9eBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9eBuildingBlock1" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<Story Self="u231e" AppliedTOCStyle="n" TrackChanges="false" StoryTitle="00.Contents" AppliedNamedGrid="n">
		<StoryPreference OpticalMarginAlignment="false" OpticalMarginSize="12" FrameType="TextFrameType" StoryOrientation="Horizontal" StoryDirection="LeftToRightDirection" />
		<InCopyExportOption IncludeGraphicProxies="true" IncludeAllResources="false" />
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/$ID/NormalParagraphStyle" SpaceAfter="30" Justification="CenterAlign">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]" Tracking="199.99999999999997">
				<Properties>
					<AppliedFont type="string">Times</AppliedFont>
				</Properties>
				<Content>CONTENTS</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<AppliedFont type="string">Times</AppliedFont>
				</Properties>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/toc">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>I	Introduction in Defence of Everything Else	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>1</Content>
				<Br />
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>II	The Maniac	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>13</Content>
				<Br />
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>III	The Suicide of Thought	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>33</Content>
				<Br />
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>IV	The Ethics of Elfland	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>53</Content>
				<Br />
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>V	The Flag of the World	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>79</Content>
				<Br />
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>VI	The Paradoxes of Christianity	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>99</Content>
				<Br />
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>VII	The Eternal Revolution	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>125</Content>
				<Br />
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>VIII	The Romance of Orthodoxy	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>153</Content>
				<Br />
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>IX	Authority and the Adventurer	</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Properties>
					<Leading type="unit">13</Leading>
				</Properties>
				<Content>175</Content>
			</CharacterStyleRange>
		</ParagraphStyleRange>
	</Story>
</Document>
"""

chapter_one = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<?aid style="50" type="snippet" readerVersion="6.0" featureSet="257" product="8.0(370)" ?>
<?aid SnippetType="InCopyInterchange"?>
<Document DOMVersion="8.0" Self="d">
	<RootCharacterStyleGroup Self="u77">
		<CharacterStyle Self="CharacterStyle/$ID/[No character style]" Imported="false" Name="$ID/[No character style]" />
	</RootCharacterStyleGroup>
	<RootParagraphStyleGroup Self="u76">
		<ParagraphStyle Self="ParagraphStyle/chapter subtitle" Name="chapter subtitle" Imported="false" NextStyle="ParagraphStyle/chapter subtitle" KeyboardShortcut="0 0" FontStyle="Italic" PointSize="9" Justification="CenterAlign">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<AppliedFont type="string">Times</AppliedFont>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/chapter title" Name="chapter title" Imported="false" NextStyle="ParagraphStyle/chapter title" KeyboardShortcut="0 0" Capitalization="SmallCaps" SpaceBefore="5" Justification="CenterAlign">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<BalanceRaggedLines type="enumeration">VeeShape</BalanceRaggedLines>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/p-first" Name="p-first" Imported="false" NextStyle="ParagraphStyle/p-first" KeyboardShortcut="0 0" DropCapCharacters="1" DropCapLines="2" FirstLineIndent="0" StartParagraph="NextFrame">
			<Properties>
				<BasedOn type="object">ParagraphStyle/p</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/p" Name="p" Imported="false" NextStyle="ParagraphStyle/p" KeyboardShortcut="0 0" PointSize="9" FirstLineIndent="12" HyphenateAfterFirst="3" HyphenateBeforeLast="3" HyphenateCapitalizedWords="false" HyphenateWordsLongerThan="6" KeepFirstLines="1" KeepLinesTogether="true" HyphenateLastWord="false" Justification="LeftJustified" HyphenateAcrossColumns="false">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<Leading type="unit">11</Leading>
				<AppliedFont type="string">Times</AppliedFont>
			</Properties>
		</ParagraphStyle>
	</RootParagraphStyleGroup>
	<TinDocumentDataObject>
		<Properties>
			<GaijiRefMaps><![CDATA[/////wAAAAAAAAAA]]></GaijiRefMaps>
		</Properties>
	</TinDocumentDataObject>
	<CrossReferenceFormat Self="u96" Name="Full Paragraph &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u96BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock1" BlockType="FullParagraphBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u97" Name="Full Paragraph" AppliedCharacterStyle="n">
		<BuildingBlock Self="u97BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u97BuildingBlock1" BlockType="FullParagraphBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u97BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u98" Name="Paragraph Text &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u98BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock1" BlockType="ParagraphTextBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u99" Name="Paragraph Text" AppliedCharacterStyle="n">
		<BuildingBlock Self="u99BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u99BuildingBlock1" BlockType="ParagraphTextBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u99BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9a" Name="Paragraph Number &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9aBuildingBlock0" BlockType="ParagraphNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9aBuildingBlock1" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText=" on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9aBuildingBlock2" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9b" Name="Paragraph Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9bBuildingBlock0" BlockType="ParagraphNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9c" Name="Text Anchor Name &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9cBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock1" BlockType="BookmarkNameBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9d" Name="Text Anchor Name" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9dBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9dBuildingBlock1" BlockType="BookmarkNameBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9dBuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9e" Name="Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9eBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9eBuildingBlock1" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<Story Self="u2d0" AppliedTOCStyle="n" TrackChanges="false" StoryTitle="01.Chapter" AppliedNamedGrid="n">
		<StoryPreference OpticalMarginAlignment="false" OpticalMarginSize="12" FrameType="TextFrameType" StoryOrientation="Horizontal" StoryDirection="LeftToRightDirection" />
		<InCopyExportOption IncludeGraphicProxies="true" IncludeAllResources="false" />
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/chapter subtitle">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>CHAPTER I</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/chapter title">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>Introduction in Defence of Everything Else</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/p-first">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>The only possible excuse for this book is that it is an answer to a challenge. Even a bad shot is dignified when he accepts a duel. When some time ago I published a series of hasty but sincere papers, under the name of “Heretics,” several critics for whose intellect I have a warm respect (I may mention specially Mr. G.S. Street) said that it was all very well for me to tell everybody to affirm his cosmic theory, but that I had carefully avoided supporting my precepts with example. “I will begin to worry about my philosophy,” said Mr. Street, “when Mr. Chesterton has given us his.” It was perhaps an incautious suggestion to make to a person only too ready to write books upon the feeblest provocation. But after all, though Mr. Street has inspired and created this book, he need not read it. If he does read it, he will find that in its pages I have attempted in a vague and personal way, in a set of mental pictures rather than in a series of deductions, to state the philosophy in which I have come to believe. I will not call it my philosophy; for I did not make it. God and humanity made it; and it made me.</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/p">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>I have often had a fancy for writing a romance about an English yachtsman who slightly miscalculated his course and discovered England under the impression that it was a new island in the South Seas. I always find, however, that I am either too busy or too lazy to write this fine work, so I may as well give it away for the purposes of philosophical illustration. There will probably be a general impression that the man who landed (armed to the teeth and talking by signs) to plant the British flag on that barbaric temple which turned out to be the Pavilion at Brighton, felt rather a fool. I am not here concerned to deny that he looked a fool. But if you imagine that he felt a fool, or at any rate that the sense of folly was his sole or his dominant emotion, then you have not studied with sufficient delicacy the rich romantic nature of the hero of this tale. His mistake was really a most enviable mistake; and he knew it, if he was the man I take him for. What could be more delightful than to have in the same few minutes all the fascinating terrors of going abroad combined with all the humane security of coming home again? What could be better than to have all the fun of discovering South Africa without the disgusting necessity of landing there? What could be more glorious than to brace one’s self up to discover New South Wales and then realize, with a gush of happy tears, that it was really old South Wales. This at least seems to me the main problem for philosophers, and is in a manner the main problem of this book. How can we contrive to be at once astonished at the world and yet at home in it? How can this queer cosmic town, with its many-legged citizens, with its monstrous and ancient lamps, how can this world give us at once the fascination of a strange town and the comfort and honour of being our own town? To show that a faith or a philosophy is true from every standpoint would be too big an undertaking even for a much bigger book than this; it is necessary to follow one path of argument; and this is the path that I here propose to follow. I wish to set forth my faith as particularly answering this double spiritual need, the need for that mixture of the familiar and the unfamiliar which Christendom has rightly named romance. For the very word “romance” has in it the mystery and ancient meaning of Rome. Any one setting out to dispute anything ought always to begin by saying what he does not dispute. Beyond stating what he proposes to prove he should always state what he does not propose to prove. The thing I do not propose to prove, the thing I propose to take as common ground between myself and any average reader, is this desirability of an active and imaginative life, picturesque and full of a poetical curiosity, a life such as western man at any rate always seems to have desired. If a man says that extinction is better than existence or blank existence better than variety and adventure, then he is not one of the ordinary people to whom I am talking. If a man prefers nothing I can give him nothing. But nearly all people I have ever met in this western society in which I live would agree to the general proposition that we need this life of practical romance; the combination of something that is strange with something that is secure. We need so to view the world as to combine an idea of wonder and an idea of welcome. We need to be happy in this wonderland without once being merely comfortable. It is this achievement of my creed that I shall chiefly pursue in these pages.</Content>
				<Br />
				<Content>But I have a peculiar reason for mentioning the man in a yacht, who discovered England. For I am that man in a yacht. I discovered England. I do not see how this book can avoid being egotistical; and I do not quite see (to tell the truth) how it can avoid being dull. Dullness will, however, free me from the charge which I most lament; the charge of being flippant. Mere light sophistry is the thing that I happen to despise most of all things, and it is perhaps a wholesome fact that this is the thing of which I am generally accused. I know nothing so contemptible as a mere paradox; a mere ingenious defence of the indefensible. If it were true (as has been said) that Mr. Bernard Shaw lived upon paradox, then he ought to be a mere common millionaire; for a man of his mental activity could invent a sophistry every six minutes. It is as easy as lying; because it is lying. The truth is, of course, that Mr. Shaw is cruelly hampered by the fact that he cannot tell any lie unless he thinks it is the truth. I find myself under the same intolerable bondage. I never in my life said anything merely because I thought it funny; though, of course, I have had ordinary human vain-glory, and may have thought it funny because I had said it. It is one thing to describe an interview with a gorgon or a griffin, a creature who does not exist. It is another thing to discover that the rhinoceros does exist and then take pleasure in the fact that he looks as if he didn’t. One searches for truth, but it may be that one pursues instinctively the more extraordinary truths. And I offer this book with the heartiest sentiments to all the jolly people who hate what I write, and regard it (very justly, for all I know), as a piece of poor clowning or a single tiresome joke.</Content>
				<Br />
				<Content>For if this book is a joke it is a joke against me. I am the man who with the utmost daring discovered what had been discovered before. If there is an element of farce in what follows, the farce is at my own expense; for this book explains how I fancied I was the first to set foot in Brighton and then found I was the last. It recounts my elephantine adventures in pursuit of the obvious. No one can think my case more ludicrous than I think it myself; no reader can accuse me here of trying to make a fool of him: I am the fool of this story, and no rebel shall hurl me from my throne. I freely confess all the idiotic ambitions of the end of the nineteenth century. I did, like all other solemn little boys, try to be in advance of the age. Like them I tried to be some ten minutes in advance of the truth. And I found that I was eighteen hundred years behind it. I did strain my voice with a painfully juvenile exaggeration in uttering my truths. And I was punished in the fittest and funniest way, for I have kept my truths: but I have discovered, not that they were not truths, but simply that they were not mine. When I fancied that I stood alone I was really in the ridiculous position of being backed up by all Christendom. It may be, Heaven forgive me, that I did try to be original; but I only succeeded in inventing all by myself an inferior copy of the existing traditions of civilized religion. The man from the yacht thought he was the first to find England; I thought I was the first to find Europe. I did try to found a heresy of my own; and when I had put the last touches to it, I discovered that it was orthodoxy.</Content>
				<Br />
				<Content>It may be that somebody will be entertained by the account of this happy fiasco. It might amuse a friend or an enemy to read how I gradually learnt from the truth of some stray legend or from the falsehood of some dominant philosophy, things that I might have learnt from my catechism—if I had ever learnt it. There may or may not be some entertainment in reading how I found at last in an anarchist club or a Babylonian temple what I might have found in the nearest parish church. If any one is entertained by learning how the flowers of the field or the phrases in an omnibus, the accidents of politics or the pains of youth came together in a certain order to produce a certain conviction of Christian orthodoxy, he may possibly read this book. But there is in everything a reasonable division of labour. I have written the book, and nothing on earth would induce me to read it.</Content>
				<Br />
				<Content>I add one purely pedantic note which comes, as a note naturally should, at the beginning of the book. These essays are concerned only to discuss the actual fact that the central Christian theology (sufficiently summarized in the Apostles’ Creed) is the best root of energy and sound ethics. They are not intended to discuss the very fascinating but quite different question of what is the present seat of authority for the proclamation of that creed. When the word “orthodoxy” is used here it means the Apostles’ Creed, as understood by everybody calling himself Christian until a very short time ago and the general historic conduct of those who held such a creed. I have been forced by mere space to confine myself to what I have got from this creed; I do not touch the matter much disputed among modern Christians, of where we ourselves got it. This is not an ecclesiastical treatise but a sort of slovenly autobiography. But if any one wants my opinions about the actual nature of the authority, Mr. G.S. Street has only to throw me another challenge, and I will write him another book.</Content>
			</CharacterStyleRange>
		</ParagraphStyleRange>
	</Story>
</Document>
"""

chapter_two = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<?aid style="50" type="snippet" readerVersion="6.0" featureSet="257" product="8.0(370)" ?>
<?aid SnippetType="InCopyInterchange"?>
<Document DOMVersion="8.0" Self="d">
	<RootCharacterStyleGroup Self="u77">
		<CharacterStyle Self="CharacterStyle/$ID/[No character style]" Imported="false" Name="$ID/[No character style]" />
	</RootCharacterStyleGroup>
	<RootParagraphStyleGroup Self="u76">
		<ParagraphStyle Self="ParagraphStyle/chapter subtitle" Name="chapter subtitle" Imported="false" NextStyle="ParagraphStyle/chapter subtitle" KeyboardShortcut="0 0" FontStyle="Italic" PointSize="9" Justification="CenterAlign">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<AppliedFont type="string">Times</AppliedFont>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/chapter title" Name="chapter title" Imported="false" NextStyle="ParagraphStyle/chapter title" KeyboardShortcut="0 0" Capitalization="SmallCaps" SpaceBefore="5" Justification="CenterAlign">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<BalanceRaggedLines type="enumeration">VeeShape</BalanceRaggedLines>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/p-first" Name="p-first" Imported="false" NextStyle="ParagraphStyle/p-first" KeyboardShortcut="0 0" DropCapCharacters="1" DropCapLines="2" FirstLineIndent="0" StartParagraph="NextFrame">
			<Properties>
				<BasedOn type="object">ParagraphStyle/p</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/p" Name="p" Imported="false" NextStyle="ParagraphStyle/p" KeyboardShortcut="0 0" PointSize="9" FirstLineIndent="12" HyphenateAfterFirst="3" HyphenateBeforeLast="3" HyphenateCapitalizedWords="false" HyphenateWordsLongerThan="6" KeepFirstLines="1" KeepLinesTogether="true" HyphenateLastWord="false" Justification="LeftJustified" HyphenateAcrossColumns="false">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<Leading type="unit">11</Leading>
				<AppliedFont type="string">Times</AppliedFont>
			</Properties>
		</ParagraphStyle>
	</RootParagraphStyleGroup>
	<TinDocumentDataObject>
		<Properties>
			<GaijiRefMaps><![CDATA[/////wAAAAAAAAAA]]></GaijiRefMaps>
		</Properties>
	</TinDocumentDataObject>
	<CrossReferenceFormat Self="u96" Name="Full Paragraph &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u96BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock1" BlockType="FullParagraphBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u97" Name="Full Paragraph" AppliedCharacterStyle="n">
		<BuildingBlock Self="u97BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u97BuildingBlock1" BlockType="FullParagraphBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u97BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u98" Name="Paragraph Text &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u98BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock1" BlockType="ParagraphTextBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u99" Name="Paragraph Text" AppliedCharacterStyle="n">
		<BuildingBlock Self="u99BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u99BuildingBlock1" BlockType="ParagraphTextBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u99BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9a" Name="Paragraph Number &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9aBuildingBlock0" BlockType="ParagraphNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9aBuildingBlock1" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText=" on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9aBuildingBlock2" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9b" Name="Paragraph Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9bBuildingBlock0" BlockType="ParagraphNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9c" Name="Text Anchor Name &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9cBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock1" BlockType="BookmarkNameBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9d" Name="Text Anchor Name" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9dBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9dBuildingBlock1" BlockType="BookmarkNameBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9dBuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9e" Name="Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9eBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9eBuildingBlock1" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<Story Self="u396" AppliedTOCStyle="n" TrackChanges="false" StoryTitle="02.Chapter" AppliedNamedGrid="n">
		<StoryPreference OpticalMarginAlignment="false" OpticalMarginSize="12" FrameType="TextFrameType" StoryOrientation="Horizontal" StoryDirection="LeftToRightDirection" />
		<InCopyExportOption IncludeGraphicProxies="true" IncludeAllResources="false" />
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/chapter subtitle">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>CHAPTER II</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/chapter title">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>The Maniac</Content>
			</CharacterStyleRange>
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]" Capitalization="Normal">
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/p-first">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>Thoroughly worldly people never understand even the world; they rely altogether on a few cynical maxims which are not true. Once I remember walking with a prosperous publisher, who made a remark which I had often heard before; it is, indeed, almost a motto of the modern world. Yet I had heard it once too often, and I saw suddenly that there was nothing in it. The publisher said of somebody, “That man will get on; he believes in himself.” And I remember that as I lifted my head to listen, my eye caught an omnibus on which was written “Hanwell.” I said to him, “Shall I tell you where the men are who believe most in themselves? For I can tell you. I know of men who believe in themselves more colossally than Napoleon or Caesar. I know where flames the fixed star of certainty and success. I can guide you to the thrones of the Super-men. The men who really believe in themselves are all in lunatic asylums.” He said mildly that there were a good many men after all who believed in themselves and who were not in lunatic asylums. “Yes, there are,” I retorted, “and you of all men ought to know them. That drunken poet from whom you would not take a dreary tragedy, he believed in himself. That elderly minister with an epic from whom you were hiding in a back room, he believed in himself. If you consulted your business experience instead of your ugly individualistic philosophy, you would know that believing in himself is one of the commonest signs of a rotter. Actors who can’t act believe in themselves; and debtors who won’t pay. It would be much truer to say that a man will certainly fail because he believes in himself. Complete self-confidence is not merely a sin; complete self-confidence is a weakness. Believing utterly in one’s self is a hysterical and superstitious belief like believing in Joanna Southcote: the man who has it has ‘Hanwell’ written on his face as plain as it is written on that omnibus.” And to all this my friend the publisher made this very deep and effective reply, “Well, if a man is not to believe in himself, in what is he to believe?” After a long pause I replied, “I will go home and write a book in answer to that question.” This is the book that I have written in answer to it.</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/p">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>But I think this book may well start where our argument started—in the neighbourhood of the mad-house. Modern masters of science are much impressed with the need of beginning all inquiry with a fact. The ancient masters of religion were quite equally impressed with that necessity. They began with the fact of sin—a fact as practical as potatoes. Whether or no man could be washed in miraculous waters, there was no doubt at any rate that he wanted washing. But certain religious leaders in London, not mere materialists, have begun in our day not to deny the highly disputable water, but to deny the indisputable dirt. Certain new theologians dispute original sin, which is the only part of Christian theology which can really be proved. Some followers of the Reverend R.J. Campbell, in their almost too fastidious spirituality, admit divine sinlessness, which they cannot see even in their dreams. But they essentially deny human sin, which they can see in the street. The strongest saints and the strongest sceptics alike took positive evil as the starting-point of their argument. If it be true (as it certainly is) that a man can feel exquisite happiness in skinning a cat, then the religious philosopher can only draw one of two deductions. He must either deny the existence of God, as all atheists do; or he must deny the present union between God and man, as all Christians do. The new theologians seem to think it a highly rationalistic solution to deny the cat.</Content>
				<Br />
				<Content>In this remarkable situation it is plainly not now possible (with any hope of a universal appeal) to start, as our fathers did, with the fact of sin. This very fact which was to them (and is to me) as plain as a pikestaff, is the very fact that has been specially diluted or denied. But though moderns deny the existence of sin, I do not think that they have yet denied the existence of a lunatic asylum. We all agree still that there is a collapse of the intellect as unmistakable as a falling house. Men deny hell, but not, as yet, Hanwell. For the purpose of our primary argument the one may very well stand where the other stood. I mean that as all thoughts and theories were once judged by whether they tended to make a man lose his soul, so for our present purpose all modern thoughts and theories may be judged by whether they tend to make a man lose his wits.</Content>
				<Br />
				<Content>It is true that some speak lightly and loosely of insanity as in itself attractive. But a moment’s thought will show that if disease is beautiful, it is generally some one else’s disease. A blind man may be picturesque; but it requires two eyes to see the picture. And similarly even the wildest poetry of insanity can only be enjoyed by the sane. To the insane man his insanity is quite prosaic, because it is quite true. A man who thinks himself a chicken is to himself as ordinary as a chicken. A man who thinks he is a bit of glass is to himself as dull as a bit of glass. It is the homogeneity of his mind which makes him dull, and which makes him mad. It is only because we see the irony of his idea that we think him even amusing; it is only because he does not see the irony of his idea that he is put in Hanwell at all. In short, oddities only strike ordinary people. Oddities do not strike odd people. This is why ordinary people have a much more exciting time; while odd people are always complaining of the dulness of life. This is also why the new novels die so quickly, and why the old fairy tales endure for ever. The old fairy tale makes the hero a normal human boy; it is his adventures that are startling; they startle him because he is normal. But in the modern psychological novel the hero is abnormal; the centre is not central. Hence the fiercest adventures fail to affect him adequately, and the book is monotonous. You can make a story out of a hero among dragons; but not out of a dragon among dragons. The fairy tale discusses what a sane man will do in a mad world. The sober realistic novel of to-day discusses what an essential lunatic will do in a dull world.</Content>
				<Br />
				<Content>Let us begin, then, with the mad-house; from this evil and fantastic inn let us set forth on our intellectual journey. Now, if we are to glance at the philosophy of sanity, the first thing to do in the matter is to blot out one big and common mistake. There is a notion adrift everywhere that imagination, especially mystical imagination, is dangerous to man’s mental balance. Poets are commonly spoken of as psychologically unreliable; and generally there is a vague association between wreathing laurels in your hair and sticking straws in it. Facts and history utterly contradict this view. Most of the very great poets have been not only sane, but extremely business-like; and if Shakespeare ever really held horses, it was because he was much the safest man to hold them. Imagination does not breed insanity. Exactly what does breed insanity is reason. Poets do not go mad; but chess-players do. Mathematicians go mad, and cashiers; but creative artists very seldom. I am not, as will be seen, in any sense attacking logic: I only say that this danger does lie in logic, not in imagination. Artistic paternity is as wholesome as physical paternity. Moreover, it is worthy of remark that when a poet really was morbid it was commonly because he had some weak spot of rationality on his brain. Poe, for instance, really was morbid; not because he was poetical, but because he was specially analytical. Even chess was too poetical for him; he disliked chess because it was full of knights and castles, like a poem. He avowedly preferred the black discs of draughts, because they were more like the mere black dots on a diagram. Perhaps the strongest case of all is this: that only one great English poet went mad, Cowper. And he was definitely driven mad by logic, by the ugly and alien logic of predestination. Poetry was not the disease, but the medicine; poetry partly kept him in health. He could sometimes forget the red and thirsty hell to which his hideous necessitarianism dragged him among the wide waters and the white flat lilies of the Ouse. He was damned by John Calvin; he was almost saved by John Gilpin. Everywhere we see that men do not go mad by dreaming. Critics are much madder than poets. Homer is complete and calm enough; it is his critics who tear him into extravagant tatters. Shakespeare is quite himself; it is only some of his critics who have discovered that he was somebody else. And though St. John the Evangelist saw many strange monsters in his vision, he saw no creature so wild as one of his own commentators. The general fact is simple. Poetry is sane because it floats easily in an infinite sea; reason seeks to cross the infinite sea, and so make it finite. The result is mental exhaustion, like the physical exhaustion of Mr. Holbein. To accept everything is an exercise, to understand everything a strain. The poet only desires exaltation and expansion, a world to stretch himself in. The poet only asks to get his head into the heavens. It is the logician who seeks to get the heavens into his head. And it is his head that splits.</Content>
				<Br />
				<Content>It is a small matter, but not irrelevant, that this striking mistake is commonly supported by a striking misquotation. We have all heard people cite the celebrated line of Dryden as “Great genius is to madness near allied.” But Dryden did not say that great genius was to madness near allied. Dryden was a great genius himself, and knew better. It would have been hard to find a man more romantic than he, or more sensible. What Dryden said was this, “Great wits are oft to madness near allied”; and that is true. It is the pure promptitude of the intellect that is in peril of a breakdown. Also people might remember of what sort of man Dryden was talking. He was not talking of any unworldly visionary like Vaughan or George Herbert. He was talking of a cynical man of the world, a sceptic, a diplomatist, a great practical politician. Such men are indeed to madness near allied. Their incessant calculation of their own brains and other people’s brains is a dangerous trade. It is always perilous to the mind to reckon up the mind. A flippant person has asked why we say, “As mad as a hatter.” A more flippant person might answer that a hatter is mad because he has to measure the human head.</Content>
				<Br />
				<Content>And if great reasoners are often maniacal, it is equally true that maniacs are commonly great reasoners. When I was engaged in a controversy with the Clarion on the matter of free will, that able writer Mr. R.B. Suthers said that free will was lunacy, because it meant causeless actions, and the actions of a lunatic would be causeless. I do not dwell here upon the disastrous lapse in determinist logic. Obviously if any actions, even a lunatic’s, can be causeless, determinism is done for. If the chain of causation can be broken for a madman, it can be broken for a man. But my purpose is to point out something more practical. It was natural, perhaps, that a modern Marxian Socialist should not know anything about free will. But it was certainly remarkable that a modern Marxian Socialist should not know anything about lunatics. Mr. Suthers evidently did not know anything about lunatics. The last thing that can be said of a lunatic is that his actions are causeless. If any human acts may loosely be called causeless, they are the minor acts of a healthy man; whistling as he walks; slashing the grass with a stick; kicking his heels or rubbing his hands. It is the happy man who does the useless things; the sick man is not strong enough to be idle. It is exactly such careless and causeless actions that the madman could never understand; for the madman (like the determinist) generally sees too much cause in everything. The madman would read a conspiratorial significance into those empty activities. He would think that the lopping of the grass was an attack on private property. He would think that the kicking of the heels was a signal to an accomplice. If the madman could for an instant become careless, he would become sane. Every one who has had the misfortune to talk with people in the heart or on the edge of mental disorder, knows that their most sinister quality is a horrible clarity of detail; a connecting of one thing with another in a map more elaborate than a maze. If you argue with a madman, it is extremely probable that you will get the worst of it; for in many ways his mind moves all the quicker for not being delayed by the things that go with good judgment. He is not hampered by a sense of humour or by charity, or by the dumb certainties of experience. He is the more logical for losing certain sane affections. Indeed, the common phrase for insanity is in this respect a misleading one. The madman is not the man who has lost his reason. The madman is the man who has lost everything except his reason.</Content>
				<Br />
				<Content>The madman’s explanation of a thing is always complete, and often in a purely rational sense satisfactory. Or, to speak more strictly, the insane explanation, if not conclusive, is at least unanswerable; this may be observed specially in the two or three commonest kinds of madness. If a man says (for instance) that men have a conspiracy against him, you cannot dispute it except by saying that all the men deny that they are conspirators; which is exactly what conspirators would do. His explanation covers the facts as much as yours. Or if a man says that he is the rightful King of England, it is no complete answer to say that the existing authorities call him mad; for if he were King of England that might be the wisest thing for the existing authorities to do. Or if a man says that he is Jesus Christ, it is no answer to tell him that the world denies his divinity; for the world denied Christ’s.</Content>
				<Br />
				<Content>Nevertheless he is wrong. But if we attempt to trace his error in exact terms, we shall not find it quite so easy as we had supposed. Perhaps the nearest we can get to expressing it is to say this: that his mind moves in a perfect but narrow circle. A small circle is quite as infinite as a large circle; but, though it is quite as infinite, it is not so large. In the same way the insane explanation is quite as complete as the sane one, but it is not so large. A bullet is quite as round as the world, but it is not the world. There is such a thing as a narrow universality; there is such a thing as a small and cramped eternity; you may see it in many modern religions. Now, speaking quite externally and empirically, we may say that the strongest and most unmistakable mark of madness is this combination between a logical completeness and a spiritual contraction. The lunatic’s theory explains a large number of things, but it does not explain them in a large way. I mean that if you or I were dealing with a mind that was growing morbid, we should be chiefly concerned not so much to give it arguments as to give it air, to convince it that there was something cleaner and cooler outside the suffocation of a single argument. Suppose, for instance, it were the first case that I took as typical; suppose it were the case of a man who accused everybody of conspiring against him. If we could express our deepest feelings of protest and appeal against this obsession, I suppose we should say something like this: “Oh, I admit that you have your case and have it by heart, and that many things do fit into other things as you say. I admit that your explanation explains a great deal; but what a great deal it leaves out! Are there no other stories in the world except yours; and are all men busy with your business? Suppose we grant the details; perhaps when the man in the street did not seem to see you it was only his cunning; perhaps when the policeman asked you your name it was only because he knew it already. But how much happier you would be if you only knew that these people cared nothing about you! How much larger your life would be if your self could become smaller in it; if you could really look at other men with common curiosity and pleasure; if you could see them walking as they are in their sunny selfishness and their virile indifference! You would begin to be interested in them, because they were not interested in you. You would break out of this tiny and tawdry theatre in which your own little plot is always being played, and you would find yourself under a freer sky, in a street full of splendid strangers.” Or suppose it were the second case of madness, that of a man who claims the crown, your impulse would be to answer, “All right! Perhaps you know that you are the King of England; but why do you care? Make one magnificent effort and you will be a human being and look down on all the kings of the earth.” Or it might be the third case, of the madman who called himself Christ. If we said what we felt, we should say, “So you are the Creator and Redeemer of the world: but what a small world it must be! What a little heaven you must inhabit, with angels no bigger than butterflies! How sad it must be to be God; and an inadequate God! Is there really no life fuller and no love more marvellous than yours; and is it really in your small and painful pity that all flesh must put its faith? How much happier you would be, how much more of you there would be, if the hammer of a higher God could smash your small cosmos, scattering the stars like spangles, and leave you in the open, free like other men to look up as well as down!”</Content>
				<Br />
				<Content>And it must be remembered that the most purely practical science does take this view of mental evil; it does not seek to argue with it like a heresy, but simply to snap it like a spell. Neither modern science nor ancient religion believes in complete free thought. Theology rebukes certain thoughts by calling them blasphemous. Science rebukes certain thoughts by calling them morbid. For example, some religious societies discouraged men more or less from thinking about sex. The new scientific society definitely discourages men from thinking about death; it is a fact, but it is considered a morbid fact. And in dealing with those whose morbidity has a touch of mania, modern science cares far less for pure logic than a dancing Dervish. In these cases it is not enough that the unhappy man should desire truth; he must desire health. Nothing can save him but a blind hunger for normality, like that of a beast. A man cannot think himself out of mental evil; for it is actually the organ of thought that has become diseased, ungovernable, and, as it were, independent. He can only be saved by will or faith. The moment his mere reason moves, it moves in the old circular rut; he will go round and round his logical circle, just as a man in a third-class carriage on the Inner Circle will go round and round the Inner Circle unless he performs the voluntary, vigorous, and mystical act of getting out at Gower Street. Decision is the whole business here; a door must be shut for ever. Every remedy is a desperate remedy. Every cure is a miraculous cure. Curing a madman is not arguing with a philosopher; it is casting out a devil. And however quietly doctors and psychologists may go to work in the matter, their attitude is profoundly intolerant—as intolerant as Bloody Mary. Their attitude is really this: that the man must stop thinking, if he is to go on living. Their counsel is one of intellectual amputation. If thy head offend thee, cut it off; for it is better, not merely to enter the Kingdom of Heaven as a child, but to enter it as an imbecile, rather than with your whole intellect to be cast into hell—or into Hanwell.</Content>
				<Br />
				<Content>Such is the madman of experience; he is commonly a reasoner, frequently a successful reasoner. Doubtless he could be vanquished in mere reason, and the case against him put logically. But it can be put much more precisely in more general and even æsthetic terms. He is in the clean and well-lit prison of one idea: he is sharpened to one painful point. He is without healthy hesitation and healthy complexity. Now, as I explain in the introduction, I have determined in these early chapters to give not so much a diagram of a doctrine as some pictures of a point of view. And I have described at length my vision of the maniac for this reason: that just as I am affected by the maniac, so I am affected by most modern thinkers. That unmistakable mood or note that I hear from Hanwell, I hear also from half the chairs of science and seats of learning to-day; and most of the mad doctors are mad doctors in more senses than one. They all have exactly that combination we have noted: the combination of an expansive and exhaustive reason with a contracted common sense. They are universal only in the sense that they take one thin explanation and carry it very far. But a pattern can stretch for ever and still be a small pattern. They see a chess-board white on black, and if the universe is paved with it, it is still white on black. Like the lunatic, they cannot alter their standpoint; they cannot make a mental effort and suddenly see it black on white.</Content>
				<Br />
				<Content>Take first the more obvious case of materialism. As an explanation of the world, materialism has a sort of insane simplicity. It has just the quality of the madman’s argument; we have at once the sense of it covering everything and the sense of it leaving everything out. Contemplate some able and sincere materialist, as, for instance, Mr. McCabe, and you will have exactly this unique sensation. He understands everything, and everything does not seem worth understanding. His cosmos may be complete in every rivet and cog-wheel, but still his cosmos is smaller than our world. Somehow his scheme, like the lucid scheme of the madman, seems unconscious of the alien energies and the large indifference of the earth; it is not thinking of the real things of the earth, of fighting peoples or proud mothers, or first love or fear upon the sea. The earth is so very large, and the cosmos is so very small. The cosmos is about the smallest hole that a man can hide his head in.</Content>
				<Br />
				<Content>It must be understood that I am not now discussing the relation of these creeds to truth; but, for the present, solely their relation to health. Later in the argument I hope to attack the question of objective verity; here I speak only of a phenomenon of psychology. I do not for the present attempt to prove to Haeckel that materialism is untrue, any more than I attempted to prove to the man who thought he was Christ that he was labouring under an error. I merely remark here on the fact that both cases have the same kind of completeness and the same kind of incompleteness. You can explain a man’s detention at Hanwell by an indifferent public by saying that it is the crucifixion of a god of whom the world is not worthy. The explanation does explain. Similarly you may explain the order in the universe by saying that all things, even the souls of men, are leaves inevitably unfolding on an utterly unconscious tree—the blind destiny of matter. The explanation does explain, though not, of course, so completely as the madman’s. But the point here is that the normal human mind not only objects to both, but feels to both the same objection. Its approximate statement is that if the man in Hanwell is the real God, he is not much of a god. And, similarly, if the cosmos of the materialist is the real cosmos, it is not much of a cosmos. The thing has shrunk. The deity is less divine than many men; and (according to Haeckel) the whole of life is something much more grey, narrow, and trivial than many separate aspects of it. The parts seem greater than the whole.</Content>
				<Br />
				<Content>For we must remember that the materialist philosophy (whether true or not) is certainly much more limiting than any religion. In one sense, of course, all intelligent ideas are narrow. They cannot be broader than themselves. A Christian is only restricted in the same sense that an atheist is restricted. He cannot think Christianity false and continue to be a Christian; and the atheist cannot think atheism false and continue to be an atheist. But as it happens, there is a very special sense in which materialism has more restrictions than spiritualism. Mr. McCabe thinks me a slave because I am not allowed to believe in determinism. I think Mr. McCabe a slave because he is not allowed to believe in fairies. But if we examine the two vetoes we shall see that his is really much more of a pure veto than mine. The Christian is quite free to believe that there is a considerable amount of settled order and inevitable development in the universe. But the materialist is not allowed to admit into his spotless machine the slightest speck of spiritualism or miracle. Poor Mr. McCabe is not allowed to retain even the tiniest imp, though it might be hiding in a pimpernel. The Christian admits that the universe is manifold and even miscellaneous, just as a sane man knows that he is complex. The sane man knows that he has a touch of the beast, a touch of the devil, a touch of the saint, a touch of the citizen. Nay, the really sane man knows that he has a touch of the madman. But the materialist’s world is quite simple and solid, just as the madman is quite sure he is sane. The materialist is sure that history has been simply and solely a chain of causation, just as the interesting person before mentioned is quite sure that he is simply and solely a chicken. Materialists and madmen never have doubts.</Content>
				<Br />
				<Content>Spiritual doctrines do not actually limit the mind as do materialistic denials. Even if I believe in immortality I need not think about it. But if I disbelieve in immortality I must not think about it. In the first case the road is open and I can go as far as I like; in the second the road is shut. But the case is even stronger, and the parallel with madness is yet more strange. For it was our case against the exhaustive and logical theory of the lunatic that, right or wrong, it gradually destroyed his humanity. Now it is the charge against the main deductions of the materialist that, right or wrong, they gradually destroy his humanity; I do not mean only kindness, I mean hope, courage, poetry, initiative, all that is human. For instance, when materialism leads men to complete fatalism (as it generally does), it is quite idle to pretend that it is in any sense a liberating force. It is absurd to say that you are especially advancing freedom when you only use free thought to destroy free will. The determinists come to bind, not to loose. They may well call their law the “chain” of causation. It is the worst chain that ever fettered a human being. You may use the language of liberty, if you like, about materialistic teaching, but it is obvious that this is just as inapplicable to it as a whole as the same language when applied to a man locked up in a mad-house. You may say, if you like, that the man is free to think himself a poached egg. But it is surely a more massive and important fact that if he is a poached egg he is not free to eat, drink, sleep, walk, or smoke a cigarette. Similarly you may say, if you like, that the bold determinist speculator is free to disbelieve in the reality of the will. But it is a much more massive and important fact that he is not free to praise, to curse, to thank, to justify, to urge, to punish, to resist temptations, to incite mobs, to make New Year resolutions, to pardon sinners, to rebuke tyrants, or even to say “thank you” for the mustard.</Content>
				<Br />
				<Content>In passing from this subject I may note that there is a queer fallacy to the effect that materialistic fatalism is in some way favourable to mercy, to the abolition of cruel punishments or punishments of any kind. This is startlingly the reverse of the truth. It is quite tenable that the doctrine of necessity makes no difference at all; that it leaves the flogger flogging and the kind friend exhorting as before. But obviously if it stops either of them it stops the kind exhortation. That the sins are inevitable does not prevent punishment; if it prevents anything it prevents persuasion. Determinism is quite as likely to lead to cruelty as it is certain to lead to cowardice. Determinism is not inconsistent with the cruel treatment of criminals. What it is (perhaps) inconsistent with is the generous treatment of criminals; with any appeal to their better feelings or encouragement in their moral struggle. The determinist does not believe in appealing to the will, but he does believe in changing the environment. He must not say to the sinner, “Go and sin no more,” because the sinner cannot help it. But he can put him in boiling oil; for boiling oil is an environment. Considered as a figure, therefore, the materialist has the fantastic outline of the figure of the madman. Both take up a position at once unanswerable and intolerable.</Content>
				<Br />
				<Content>Of course it is not only of the materialist that all this is true. The same would apply to the other extreme of speculative logic. There is a sceptic far more terrible than he who believes that everything began in matter. It is possible to meet the sceptic who believes that everything began in himself. He doubts not the existence of angels or devils, but the existence of men and cows. For him his own friends are a mythology made up by himself. He created his own father and his own mother. This horrible fancy has in it something decidedly attractive to the somewhat mystical egoism of our day. That publisher who thought that men would get on if they believed in themselves, those seekers after the Superman who are always looking for him in the looking-glass, those writers who talk about impressing their personalities instead of creating life for the world, all these people have really only an inch between them and this awful emptiness. Then when this kindly world all round the man has been blackened out like a lie; when friends fade into ghosts, and the foundations of the world fail; then when the man, believing in nothing and in no man, is alone in his own nightmare, then the great individualistic motto shall be written over him in avenging irony. The stars will be only dots in the blackness of his own brain; his mother’s face will be only a sketch from his own insane pencil on the walls of his cell. But over his cell shall be written, with dreadful truth, “He believes in himself.”</Content>
				<Br />
				<Content>All that concerns us here, however, is to note that this panegoistic extreme of thought exhibits the same paradox as the other extreme of materialism. It is equally complete in theory and equally crippling in practice. For the sake of simplicity, it is easier to state the notion by saying that a man can believe that he is always in a dream. Now, obviously there can be no positive proof given to him that he is not in a dream, for the simple reason that no proof can be offered that might not be offered in a dream. But if the man began to burn down London and say that his housekeeper would soon call him to breakfast, we should take him and put him with other logicians in a place which has often been alluded to in the course of this chapter. The man who cannot believe his senses, and the man who cannot believe anything else, are both insane, but their insanity is proved not by any error in their argument, but by the manifest mistake of their whole lives. They have both locked themselves up in two boxes, painted inside with the sun and stars; they are both unable to get out, the one into the health and happiness of heaven, the other even into the health and happiness of the earth. Their position is quite reasonable; nay, in a sense it is infinitely reasonable, just as a threepenny bit is infinitely circular. But there is such a thing as a mean infinity, a base and slavish eternity. It is amusing to notice that many of the moderns, whether sceptics or mystics, have taken as their sign a certain eastern symbol, which is the very symbol of this ultimate nullity. When they wish to represent eternity, they represent it by a serpent with his tail in his mouth. There is a startling sarcasm in the image of that very unsatisfactory meal. The eternity of the material fatalists, the eternity of the eastern pessimists, the eternity of the supercilious theosophists and higher scientists of to-day is, indeed, very well presented by a serpent eating his tail, a degraded animal who destroys even himself.</Content>
				<Br />
				<Content>This chapter is purely practical and is concerned with what actually is the chief mark and element of insanity; we may say in summary that it is reason used without root, reason in the void. The man who begins to think without the proper first principles goes mad, the man who begins to think at the wrong end. And for the rest of these pages we have to try and discover what is the right end. But we may ask in conclusion, if this be what drives men mad, what is it that keeps them sane? By the end of this book I hope to give a definite, some will think a far too definite, answer. But for the moment it is possible in the same solely practical manner to give a general answer touching what in actual human history keeps men sane. Mysticism keeps men sane. As long as you have mystery you have health; when you destroy mystery you create morbidity. The ordinary man has always been sane because the ordinary man has always been a mystic. He has permitted the twilight. He has always had one foot in earth and the other in fairyland. He has always left himself free to doubt his gods; but (unlike the agnostic of to-day) free also to believe in them. He has always cared more for truth than for consistency. If he saw two truths that seemed to contradict each other, he would take the two truths and the contradiction along with them. His spiritual sight is stereoscopic, like his physical sight: he sees two different pictures at once and yet sees all the better for that. Thus he has always believed that there was such a thing as fate, but such a thing as free will also. Thus he believed that children were indeed the kingdom of heaven, but nevertheless ought to be obedient to the kingdom of earth. He admired youth because it was young and age because it was not. It is exactly this balance of apparent contradictions that has been the whole buoyancy of the healthy man. The whole secret of mysticism is this: that man can understand everything by the help of what he does not understand. The morbid logician seeks to make everything lucid, and succeeds in making everything mysterious. The mystic allows one thing to be mysterious, and everything else becomes lucid. The determinist makes the theory of causation quite clear, and then finds that he cannot say “if you please” to the housemaid. The Christian permits free will to remain a sacred mystery; but because of this his relations with the housemaid become of a sparkling and crystal clearness. He puts the seed of dogma in a central darkness; but it branches forth in all directions with abounding natural health. As we have taken the circle as the symbol of reason and madness, we may very well take the cross as the symbol at once of mystery and of health. Buddhism is centripetal, but Christianity is centrifugal: it breaks out. For the circle is perfect and infinite in its nature; but it is fixed for ever in its size; it can never be larger or smaller. But the cross, though it has at its heart a collision and a contradiction, can extend its four arms for ever without altering its shape. Because it has a paradox in its centre it can grow without changing. The circle returns upon itself and is bound. The cross opens its arms to the four winds; it is a signpost for free travellers.</Content>
				<Br />
				<Content>Symbols alone are of even a cloudy value in speaking of this deep matter; and another symbol from physical nature will express sufficiently well the real place of mysticism before mankind. The one created thing which we cannot look at is the one thing in the light of which we look at everything. Like the sun at noonday, mysticism explains everything else by the blaze of its own victorious invisibility. Detached intellectualism is (in the exact sense of a popular phrase) all moonshine; for it is light without heat, and it is secondary light, reflected from a dead world. But the Greeks were right when they made Apollo the god both of imagination and of sanity; for he was both the patron of poetry and the patron of healing. Of necessary dogmas and a special creed I shall speak later. But that transcendentalism by which all men live has primarily much the position of the sun in the sky. We are conscious of it as of a kind of splendid confusion; it is something both shining and shapeless, at once a blaze and a blur. But the circle of the moon is as clear and unmistakable, as recurrent and inevitable, as the circle of Euclid on a blackboard. For the moon is utterly reasonable; and the moon is the mother of lunatics and has given to them all her name.</Content>
			</CharacterStyleRange>
		</ParagraphStyleRange>
	</Story>
</Document>
"""

chapter_three = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<?aid style="50" type="snippet" readerVersion="6.0" featureSet="257" product="8.0(370)" ?>
<?aid SnippetType="InCopyInterchange"?>
<Document DOMVersion="8.0" Self="d">
	<RootCharacterStyleGroup Self="u77">
		<CharacterStyle Self="CharacterStyle/$ID/[No character style]" Imported="false" Name="$ID/[No character style]" />
	</RootCharacterStyleGroup>
	<RootParagraphStyleGroup Self="u76">
		<ParagraphStyle Self="ParagraphStyle/chapter subtitle" Name="chapter subtitle" Imported="false" NextStyle="ParagraphStyle/chapter subtitle" KeyboardShortcut="0 0" FontStyle="Italic" PointSize="9" Justification="CenterAlign">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<AppliedFont type="string">Times</AppliedFont>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/chapter title" Name="chapter title" Imported="false" NextStyle="ParagraphStyle/chapter title" KeyboardShortcut="0 0" Capitalization="SmallCaps" SpaceBefore="5" Justification="CenterAlign">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<BalanceRaggedLines type="enumeration">VeeShape</BalanceRaggedLines>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/p-first" Name="p-first" Imported="false" NextStyle="ParagraphStyle/p-first" KeyboardShortcut="0 0" DropCapCharacters="1" DropCapLines="2" FirstLineIndent="0" StartParagraph="NextFrame">
			<Properties>
				<BasedOn type="object">ParagraphStyle/p</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/p" Name="p" Imported="false" NextStyle="ParagraphStyle/p" KeyboardShortcut="0 0" PointSize="9" FirstLineIndent="12" HyphenateAfterFirst="3" HyphenateBeforeLast="3" HyphenateCapitalizedWords="false" HyphenateWordsLongerThan="6" KeepFirstLines="1" KeepLinesTogether="true" HyphenateLastWord="false" Justification="LeftJustified" HyphenateAcrossColumns="false">
			<Properties>
				<BasedOn type="string">$ID/[No paragraph style]</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
				<Leading type="unit">11</Leading>
				<AppliedFont type="string">Times</AppliedFont>
			</Properties>
		</ParagraphStyle>
		<ParagraphStyle Self="ParagraphStyle/block-quote" Name="block-quote" Imported="false" NextStyle="ParagraphStyle/block-quote" KeyboardShortcut="0 0" LeftIndent="24" RightIndent="24" FirstLineIndent="0" SpaceBefore="3" SpaceAfter="3" Justification="LeftAlign">
			<Properties>
				<BasedOn type="object">ParagraphStyle/p</BasedOn>
				<PreviewColor type="enumeration">Nothing</PreviewColor>
			</Properties>
		</ParagraphStyle>
	</RootParagraphStyleGroup>
	<TinDocumentDataObject>
		<Properties>
			<GaijiRefMaps><![CDATA[/////wAAAAAAAAAA]]></GaijiRefMaps>
		</Properties>
	</TinDocumentDataObject>
	<CrossReferenceFormat Self="u96" Name="Full Paragraph &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u96BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock1" BlockType="FullParagraphBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u96BuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u97" Name="Full Paragraph" AppliedCharacterStyle="n">
		<BuildingBlock Self="u97BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u97BuildingBlock1" BlockType="FullParagraphBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u97BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u98" Name="Paragraph Text &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u98BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock1" BlockType="ParagraphTextBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u98BuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u99" Name="Paragraph Text" AppliedCharacterStyle="n">
		<BuildingBlock Self="u99BuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u99BuildingBlock1" BlockType="ParagraphTextBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u99BuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9a" Name="Paragraph Number &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9aBuildingBlock0" BlockType="ParagraphNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9aBuildingBlock1" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText=" on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9aBuildingBlock2" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9b" Name="Paragraph Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9bBuildingBlock0" BlockType="ParagraphNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9c" Name="Text Anchor Name &amp; Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9cBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock1" BlockType="BookmarkNameBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot; on page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9cBuildingBlock3" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9d" Name="Text Anchor Name" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9dBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9dBuildingBlock1" BlockType="BookmarkNameBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9dBuildingBlock2" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="&quot;" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<CrossReferenceFormat Self="u9e" Name="Page Number" AppliedCharacterStyle="n">
		<BuildingBlock Self="u9eBuildingBlock0" BlockType="CustomStringBuildingBlock" AppliedCharacterStyle="n" CustomText="page " AppliedDelimiter="$ID/" IncludeDelimiter="false" />
		<BuildingBlock Self="u9eBuildingBlock1" BlockType="PageNumberBuildingBlock" AppliedCharacterStyle="n" CustomText="$ID/" AppliedDelimiter="$ID/" IncludeDelimiter="false" />
	</CrossReferenceFormat>
	<Story Self="u651" AppliedTOCStyle="n" TrackChanges="false" StoryTitle="03.Chapter" AppliedNamedGrid="n">
		<StoryPreference OpticalMarginAlignment="false" OpticalMarginSize="12" FrameType="TextFrameType" StoryOrientation="Horizontal" StoryDirection="LeftToRightDirection" />
		<InCopyExportOption IncludeGraphicProxies="true" IncludeAllResources="false" />
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/chapter subtitle">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>CHAPTER III</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/chapter title">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>The Suicide of Thought</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/p-first">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>The phrases of the street are not only forcible but subtle: for a figure of speech can often get into a crack too small for a definition. Phrases like “put out” or “off colour” might have been coined by Mr. Henry James in an agony of verbal precision. And there is no more subtle truth than that of the everyday phrase about a man having “his heart in the right place.” It involves the idea of normal proportion; not only does a certain function exist, but it is rightly related to other functions. Indeed, the negation of this phrase would describe with peculiar accuracy the somewhat morbid mercy and perverse tenderness of the most representative moderns. If, for instance, I had to describe with fairness the character of Mr. Bernard Shaw, I could not express myself more exactly than by saying that he has a heroically large and generous heart; but not a heart in the right place. And this is so of the typical society of our time.</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/p">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>The modern world is not evil; in some ways the modern world is far too good. It is full of wild and wasted virtues. When a religious scheme is shattered (as Christianity was shattered at the Reformation), it is not merely the vices that are let loose. The vices are, indeed, let loose, and they wander and do damage. But the virtues are let loose also; and the virtues wander more wildly, and the virtues do more terrible damage. The modern world is full of the old Christian virtues gone mad. The virtues have gone mad because they have been isolated from each other and are wandering alone. Thus some scientists care for truth; and their truth is pitiless. Thus some humanitarians only care for pity; and their pity (I am sorry to say) is often untruthful. For example, Mr. Blatchford attacks Christianity because he is mad on one Christian virtue: the merely mystical and almost irrational virtue of charity. He has a strange idea that he will make it easier to forgive sins by saying that there are no sins to forgive. Mr. Blatchford is not only an early Christian, he is the only early Christian who ought really to have been eaten by lions. For in his case the pagan accusation is really true: his mercy would mean mere anarchy. He really is the enemy of the human race—because he is so human. As the other extreme, we may take the acrid realist, who has deliberately killed in himself all human pleasure in happy tales or in the healing of the heart. Torquemada tortured people physically for the sake of moral truth. Zola tortured people morally for the sake of physical truth. But in Torquemada’s time there was at least a system that could to some extent make righteousness and peace kiss each other. Now they do not even bow. But a much stronger case than these two of truth and pity can be found in the remarkable case of the dislocation of humility.</Content>
				<Br />
				<Content>It is only with one aspect of humility that we are here concerned. Humility was largely meant as a restraint upon the arrogance and infinity of the appetite of man. He was always out-stripping his mercies with his own newly invented needs. His very power of enjoyment destroyed half his joys. By asking for pleasure, he lost the chief pleasure; for the chief pleasure is surprise. Hence it became evident that if a man would make his world large, he must be always making himself small. Even the haughty visions, the tall cities, and the toppling pinnacles are the creations of humility. Giants that tread down forests like grass are the creations of humility. Towers that vanish upwards above the loneliest star are the creations of humility. For towers are not tall unless we look up at them; and giants are not giants unless they are larger than we. All this gigantesque imagination, which is, perhaps, the mightiest of the pleasures of man, is at bottom entirely humble. It is impossible without humility to enjoy anything—even pride.</Content>
				<Br />
				<Content>But what we suffer from to-day is humility in the wrong place. Modesty has moved from the organ of ambition. Modesty has settled upon the organ of conviction; where it was never meant to be. A man was meant to be doubtful about himself, but undoubting about the truth; this has been exactly reversed. Nowadays the part of a man that a man does assert is exactly the part he ought not to assert—himself. The part he doubts is exactly the part he ought not to doubt—the Divine Reason. Huxley preached a humility content to learn from Nature. But the new sceptic is so humble that he doubts if he can even learn. Thus we should be wrong if we had said hastily that there is no humility typical of our time. The truth is that there is a real humility typical of our time; but it so happens that it is practically a more poisonous humility than the wildest prostrations of the ascetic. The old humility was a spur that prevented a man from stopping; not a nail in his boot that prevented him from going on. For the old humility made a man doubtful about his efforts, which might make him work harder. But the new humility makes a man doubtful about his aims, which will make him stop working altogether.</Content>
				<Br />
				<Content>At any street corner we may meet a man who utters the frantic and blasphemous statement that he may be wrong. Every day one comes across somebody who says that of course his view may not be the right one. Of course his view must be the right one, or it is not his view. We are on the road to producing a race of men too mentally modest to believe in the multiplication table. We are in danger of seeing philosophers who doubt the law of gravity as being a mere fancy of their own. Scoffers of old time were too proud to be convinced; but these are too humble to be convinced. The meek do inherit the earth; but the modern sceptics are too meek even to claim their inheritance. It is exactly this intellectual helplessness which is our second problem.</Content>
				<Br />
				<Content>The last chapter has been concerned only with a fact of observation: that what peril of morbidity there is for man comes rather from his reason than his imagination. It was not meant to attack the authority of reason; rather it is the ultimate purpose to defend it. For it needs defence. The whole modern world is at war with reason; and the tower already reels.</Content>
				<Br />
				<Content>The sages, it is often said, can see no answer to the riddle of religion. But the trouble with our sages is not that they cannot see the answer; it is that they cannot even see the riddle. They are like children so stupid as to notice nothing paradoxical in the playful assertion that a door is not a door. The modern latitudinarians speak, for instance, about authority in religion not only as if there were no reason in it, but as if there had never been any reason for it. Apart from seeing its philosophical basis, they cannot even see its historical cause. Religious authority has often, doubtless, been oppressive or unreasonable; just as every legal system (and especially our present one) has been callous and full of a cruel apathy. It is rational to attack the police; nay, it is glorious. But the modern critics of religious authority are like men who should attack the police without ever having heard of burglars. For there is a great and possible peril to the human mind: a peril as practical as burglary. Against it religious authority was reared, rightly or wrongly, as a barrier. And against it something certainly must be reared as a barrier, if our race is to avoid ruin.</Content>
				<Br />
				<Content>That peril is that the human intellect is free to destroy itself. Just as one generation could prevent the very existence of the next generation, by all entering a monastery or jumping into the sea, so one set of thinkers can in some degree prevent further thinking by teaching the next generation that there is no validity in any human thought. It is idle to talk always of the alternative of reason and faith. Reason is itself a matter of faith. It is an act of faith to assert that our thoughts have any relation to reality at all. If you are merely a sceptic, you must sooner or later ask yourself the question, “Why should anything go right; even observation and deduction? Why should not good logic be as misleading as bad logic? They are both movements in the brain of a bewildered ape?” The young sceptic says, “I have a right to think for myself.” But the old sceptic, the complete sceptic, says, “I have no right to think for myself. I have no right to think at all.”</Content>
				<Br />
				<Content>There is a thought that stops thought. That is the only thought that ought to be stopped. That is the ultimate evil against which all religious authority was aimed. It only appears at the end of decadent ages like our own: and already Mr. H.G. Wells has raised its ruinous banner; he has written a delicate piece of scepticism called “Doubts of the Instrument.” In this he questions the brain itself, and endeavours to remove all reality from all his own assertions, past, present, and to come. But it was against this remote ruin that all the military systems in religion were originally ranked and ruled. The creeds and the crusades, the hierarchies and the horrible persecutions were not organized, as is ignorantly said, for the suppression of reason. They were organized for the difficult defence of reason. Man, by a blind instinct, knew that if once things were wildly questioned, reason could be questioned first. The authority of priests to absolve, the authority of popes to define the authority, even of inquisitors to terrify: these were all only dark defences erected round one central authority, more undemonstrable, more supernatural than all—the authority of a man to think. We know now that this is so; we have no excuse for not knowing it. For we can hear scepticism crashing through the old ring of authorities, and at the same moment we can see reason swaying upon her throne. In so far as religion is gone, reason is going. For they are both of the same primary and authoritative kind. They are both methods of proof which cannot themselves be proved. And in the act of destroying the idea of Divine authority we have largely destroyed the idea of that human authority by which we do a long-division sum. With a long and sustained tug we have attempted to pull the mitre off pontifical man; and his head has come off with it.</Content>
				<Br />
				<Content>Lest this should be called loose assertion, it is perhaps desirable, though dull, to run rapidly through the chief modern fashions of thought which have this effect of stopping thought itself. Materialism and the view of everything as a personal illusion have some such effect; for if the mind is mechanical, thought cannot be very exciting, and if the cosmos is unreal, there is nothing to think about. But in these cases the effect is indirect and doubtful. In some cases it is direct and clear; notably in the case of what is generally called evolution.</Content>
				<Br />
				<Content>Evolution is a good example of that modern intelligence which, if it destroys anything, destroys itself. Evolution is either an innocent scientific description of how certain earthly things came about; or, if it is anything more than this, it is an attack upon thought itself. If evolution destroys anything, it does not destroy religion but rationalism. If evolution simply means that a positive thing called an ape turned very slowly into a positive thing called a man, then it is stingless for the most orthodox; for a personal God might just as well do things slowly as quickly, especially if, like the Christian God, he were outside time. But if it means anything more, it means that there is no such thing as an ape to change, and no such thing as a man for him to change into. It means that there is no such thing as a thing. At best, there is only one thing, and that is a flux of everything and anything. This is an attack not upon the faith, but upon the mind; you cannot think if there are no things to think about. You cannot think if you are not separate from the subject of thought. Descartes said, “I think; therefore I am.” The philosophic evolutionist reverses and negatives the epigram. He says, “I am not; therefore I cannot think.”</Content>
				<Br />
				<Content>Then there is the opposite attack on thought: that urged by Mr. H.G. Wells when he insists that every separate thing is “unique,” and there are no categories at all. This also is merely destructive. Thinking means connecting things, and stops if they cannot be connected. It need hardly be said that this scepticism forbidding thought necessarily forbids speech; a man cannot open his mouth without contradicting it. Thus when Mr. Wells says (as he did somewhere), “All chairs are quite different,” he utters not merely a misstatement, but a contradiction in terms. If all chairs were quite different, you could not call them “all chairs.”</Content>
				<Br />
				<Content>Akin to these is the false theory of progress, which maintains that we alter the test instead of trying to pass the test. We often hear it said, for instance, “What is right in one age is wrong in another.” This is quite reasonable, if it means that there is a fixed aim, and that certain methods attain at certain times and not at other times. If women, say, desire to be elegant, it may be that they are improved at one time by growing fatter and at another time by growing thinner. But you cannot say that they are improved by ceasing to wish to be elegant and beginning to wish to be oblong. If the standard changes, how can there be improvement, which implies a standard? Nietzsche started a nonsensical idea that men had once sought as good what we now call evil; if it were so, we could not talk of surpassing or even falling short of them. How can you overtake Jones if you walk in the other direction? You cannot discuss whether one people has succeeded more in being miserable than another succeeded in being happy. It would be like discussing whether Milton was more puritanical than a pig is fat.</Content>
				<Br />
				<Content>It is true that a man (a silly man) might make change itself his object or ideal. But as an ideal, change itself becomes unchangeable. If the change-worshipper wishes to estimate his own progress, he must be sternly loyal to the ideal of change; he must not begin to flirt gaily with the ideal of monotony. Progress itself cannot progress. It is worth remark, in passing, that when Tennyson, in a wild and rather weak manner, welcomed the idea of infinite alteration in society, he instinctively took a metaphor which suggests an imprisoned tedium. He wrote—</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/block-quote">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>“Let the great world spin for ever down the ringing grooves of change.”</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
		<ParagraphStyleRange AppliedParagraphStyle="ParagraphStyle/p">
			<CharacterStyleRange AppliedCharacterStyle="CharacterStyle/$ID/[No character style]">
				<Content>He thought of change itself as an unchangeable groove; and so it is. Change is about the narrowest and hardest groove that a man can get into.</Content>
				<Br />
				<Content>The main point here, however, is that this idea of a fundamental alteration in the standard is one of the things that make thought about the past or future simply impossible. The theory of a complete change of standards in human history does not merely deprive us of the pleasure of honouring our fathers; it deprives us even of the more modern and aristocratic pleasure of despising them.</Content>
				<Br />
				<Content>This bald summary of the thought-destroying forces of our time would not be complete without some reference to pragmatism; for though I have here used and should everywhere defend the pragmatist method as a preliminary guide to truth, there is an extreme application of it which involves the absence of all truth whatever. My meaning can be put shortly thus. I agree with the pragmatists that apparent objective truth is not the whole matter; that there is an authoritative need to believe the things that are necessary to the human mind. But I say that one of those necessities precisely is a belief in objective truth. The pragmatist tells a man to think what he must think and never mind the Absolute. But precisely one of the things that he must think is the Absolute. This philosophy, indeed, is a kind of verbal paradox. Pragmatism is a matter of human needs; and one of the first of human needs is to be something more than a pragmatist. Extreme pragmatism is just as inhuman as the determinism it so powerfully attacks. The determinist (who, to do him justice, does not pretend to be a human being) makes nonsense of the human sense of actual choice. The pragmatist, who professes to be specially human, makes nonsense of the human sense of actual fact.</Content>
				<Br />
				<Content>To sum up our contention so far, we may say that the most characteristic current philosophies have not only a touch of mania, but a touch of suicidal mania. The mere questioner has knocked his head against the limits of human thought; and cracked it. This is what makes so futile the warnings of the orthodox and the boasts of the advanced about the dangerous boyhood of free thought. What we are looking at is not the boyhood of free thought; it is the old age and ultimate dissolution of free thought. It is vain for bishops and pious bigwigs to discuss what dreadful things will happen if wild scepticism runs its course. It has run its course. It is vain for eloquent atheists to talk of the great truths that will be revealed if once we see free thought begin. We have seen it end. It has no more questions to ask; it has questioned itself. You cannot call up any wilder vision than a city in which men ask themselves if they have any selves. You cannot fancy a more sceptical world than that in which men doubt if there is a world. It might certainly have reached its bankruptcy more quickly and cleanly if it had not been feebly hampered by the application of indefensible laws of blasphemy or by the absurd pretence that modern England is Christian. But it would have reached the bankruptcy anyhow. Militant atheists are still unjustly persecuted; but rather because they are an old minority than because they are a new one. Free thought has exhausted its own freedom. It is weary of its own success. If any eager freethinker now hails philosophic freedom as the dawn, he is only like the man in Mark Twain who came out wrapped in blankets to see the sun rise and was just in time to see it set. If any frightened curate still says that it will be awful if the darkness of free thought should spread, we can only answer him in the high and powerful words of Mr. Belloc, “Do not, I beseech you, be troubled about the increase of forces already in dissolution. You have mistaken the hour of the night: it is already morning.” We have no more questions left to ask. We have looked for questions in the darkest corners and on the wildest peaks. We have found all the questions that can be found. It is time we gave up looking for questions and began looking for answers.</Content>
				<Br />
				<Content>But one more word must be added. At the beginning of this preliminary negative sketch I said that our mental ruin has been wrought by wild reason, not by wild imagination. A man does not go mad because he makes a statue a mile high, but he may go mad by thinking it out in square inches. Now, one school of thinkers has seen this and jumped at it as a way of renewing the pagan health of the world. They see that reason destroys; but Will, they say, creates. The ultimate authority, they say, is in will, not in reason. The supreme point is not why a man demands a thing, but the fact that he does demand it. I have no space to trace or expound this philosophy of Will. It came, I suppose, through Nietzsche, who preached something that is called egoism. That, indeed, was simple-minded enough; for Nietzsche denied egoism simply by preaching it. To preach anything is to give it away. First, the egoist calls life a war without mercy, and then he takes the greatest possible trouble to drill his enemies in war. To preach egoism is to practise altruism. But however it began, the view is common enough in current literature. The main defence of these thinkers is that they are not thinkers; they are makers. They say that choice is itself the divine thing. Thus Mr. Bernard Shaw has attacked the old idea that men’s acts are to be judged by the standard of the desire of happiness. He says that a man does not act for his happiness, but from his will. He does not say, “Jam will make me happy,” but “I want jam.” And in all this others follow him with yet greater enthusiasm. Mr. John Davidson, a remarkable poet, is so passionately excited about it that he is obliged to write prose. He publishes a short play with several long prefaces. This is natural enough in Mr. Shaw, for all his plays are prefaces: Mr. Shaw is (I suspect) the only man on earth who has never written any poetry. But that Mr. Davidson (who can write excellent poetry) should write instead laborious metaphysics in defence of this doctrine of will, does show that the doctrine of will has taken hold of men. Even Mr. H.G. Wells has half spoken in its language; saying that one should test acts not like a thinker, but like an artist, saying, “I feel this curve is right,” or “that line shall go thus.” They are all excited; and well they may be. For by this doctrine of the divine authority of will, they think they can break out of the doomed fortress of rationalism. They think they can escape.</Content>
				<Br />
				<Content>But they cannot escape. This pure praise of volition ends in the same break up and blank as the mere pursuit of logic. Exactly as complete free thought involves the doubting of thought itself, so the acceptation of mere “willing” really paralyzes the will. Mr. Bernard Shaw has not perceived the real difference between the old utilitarian test of pleasure (clumsy, of course, and easily misstated) and that which he propounds. The real difference between the test of happiness and the test of will is simply that the test of happiness is a test and the other isn’t. You can discuss whether a man’s act in jumping over a cliff was directed towards happiness; you cannot discuss whether it was derived from will. Of course it was. You can praise an action by saying that it is calculated to bring pleasure or pain to discover truth or to save the soul. But you cannot praise an action because it shows will; for to say that is merely to say that it is an action. By this praise of will you cannot really choose one course as better than another. And yet choosing one course as better than another is the very definition of the will you are praising.</Content>
				<Br />
				<Content>The worship of will is the negation of will. To admire mere choice is to refuse to choose. If Mr. Bernard Shaw comes up to me and says, “Will something,” that is tantamount to saying, “I do not mind what you will,” and that is tantamount to saying, “I have no will in the matter.” You cannot admire will in general, because the essence of will is that it is particular. A brilliant anarchist like Mr. John Davidson feels an irritation against ordinary morality, and therefore he invokes will—will to anything. He only wants humanity to want something. But humanity does want something. It wants ordinary morality. He rebels against the law and tells us to will something or anything. But we have willed something. We have willed the law against which he rebels.</Content>
				<Br />
				<Content>All the will-worshippers, from Nietzsche to Mr. Davidson, are really quite empty of volition. They cannot will, they can hardly wish. And if any one wants a proof of this, it can be found quite easily. It can be found in this fact: that they always talk of will as something that expands and breaks out. But it is quite the opposite. Every act of will is an act of self-limitation. To desire action is to desire limitation. In that sense every act is an act of self-sacrifice. When you choose anything, you reject everything else. That objection, which men of this school used to make to the act of marriage, is really an objection to every act. Every act is an irrevocable selection and exclusion. Just as when you marry one woman you give up all the others, so when you take one course of action you give up all the other courses. If you become King of England, you give up the post of Beadle in Brompton. If you go to Rome, you sacrifice a rich suggestive life in Wimbledon. It is the existence of this negative or limiting side of will that makes most of the talk of the anarchic will-worshippers little better than nonsense. For instance, Mr. John Davidson tells us to have nothing to do with “Thou shalt not”; but it is surely obvious that “Thou shalt not” is only one of the necessary corollaries of “I will.” “I will go to the Lord Mayor’s Show, and thou shalt not stop me.” Anarchism adjures us to be bold creative artists, and care for no laws or limits. But it is impossible to be an artist and not care for laws and limits. Art is limitation; the essence of every picture is the frame. If you draw a giraffe, you must draw him with a long neck. If, in your bold creative way, you hold yourself free to draw a giraffe with a short neck, you will really find that you are not free to draw a giraffe. The moment you step into the world of facts, you step into a world of limits. You can free things from alien or accidental laws, but not from the laws of their own nature. You may, if you like, free a tiger from his bars; but do not free him from his stripes. Do not free a camel of the burden of his hump: you may be freeing him from being a camel. Do not go about as a demagogue, encouraging triangles to break out of the prison of their three sides. If a triangle breaks out of its three sides, its life comes to a lamentable end. Somebody wrote a work called “The Loves of the Triangles”; I never read it, but I am sure that if triangles ever were loved, they were loved for being triangular. This is certainly the case with all artistic creation, which is in some ways the most decisive example of pure will. The artist loves his limitations: they constitute the thing he is doing. The painter is glad that the canvas is flat. The sculptor is glad that the clay is colourless.</Content>
				<Br />
				<Content>In case the point is not clear, an historic example may illustrate it. The French Revolution was really an heroic and decisive thing, because the Jacobins willed something definite and limited. They desired the freedoms of democracy, but also all the vetoes of democracy. They wished to have votes and not to have titles. Republicanism had an ascetic side in Franklin or Robespierre as well as an expansive side in Danton or Wilkes. Therefore they have created something with a solid substance and shape, the square social equality and peasant wealth of France. But since then the revolutionary or speculative mind of Europe has been weakened by shrinking from any proposal because of the limits of that proposal. Liberalism has been degraded into liberality. Men have tried to turn “revolutionise” from a transitive to an intransitive verb. The Jacobin could tell you not only the system he would rebel against, but (what was more important) the system he would not rebel against, the system he would trust. But the new rebel is a sceptic, and will not entirely trust anything. He has no loyalty; therefore he can never be really a revolutionist. And the fact that he doubts everything really gets in his way when he wants to denounce anything. For all denunciation implies a moral doctrine of some kind; and the modern revolutionist doubts not only the institution he denounces, but the doctrine by which he denounces it. Thus he writes one book complaining that imperial oppression insults the purity of women, and then he writes another book (about the sex problem) in which he insults it himself. He curses the Sultan because Christian girls lose their virginity, and then curses Mrs. Grundy because they keep it. As a politician, he will cry out that war is a waste of life, and then, as a philosopher, that all life is waste of time. A Russian pessimist will denounce a policeman for killing a peasant, and then prove by the highest philosophical principles that the peasant ought to have killed himself. A man denounces marriage as a lie, and then denounces aristocratic profligates for treating it as a lie. He calls a flag a bauble, and then blames the oppressors of Poland or Ireland because they take away that bauble. The man of this school goes first to a political meeting, where he complains that savages are treated as if they were beasts; then he takes his hat and umbrella and goes on to a scientific meeting, where he proves that they practically are beasts. In short, the modern revolutionist, being an infinite sceptic, is always engaged in undermining his own mines. In his book on politics he attacks men for trampling on morality; in his book on ethics he attacks morality for trampling on men. Therefore the modern man in revolt has become practically useless for all purposes of revolt. By rebelling against everything he has lost his right to rebel against anything.</Content>
				<Br />
				<Content>It may be added that the same blank and bankruptcy can be observed in all fierce and terrible types of literature, especially in satire. Satire may be mad and anarchic, but it presupposes an admitted superiority in certain things over others; it presupposes a standard. When little boys in the street laugh at the fatness of some distinguished journalist, they are unconsciously assuming a standard of Greek sculpture. They are appealing to the marble Apollo. And the curious disappearance of satire from our literature is an instance of the fierce things fading for want of any principle to be fierce about. Nietzsche had some natural talent for sarcasm: he could sneer, though he could not laugh; but there is always something bodiless and without weight in his satire, simply because it has not any mass of common morality behind it. He is himself more preposterous than anything he denounces. But, indeed, Nietzsche will stand very well as the type of the whole of this failure of abstract violence. The softening of the brain which ultimately overtook him was not a physical accident. If Nietzsche had not ended in imbecility, Nietzscheism would end in imbecility. Thinking in isolation and with pride ends in being an idiot. Every man who will not have softening of the heart must at last have softening of the brain.</Content>
				<Br />
				<Content>This last attempt to evade intellectualism ends in intellectualism, and therefore in death. The sortie has failed. The wild worship of lawlessness and the materialist worship of law end in the same void. Nietzsche scales staggering mountains, but he turns up ultimately in Tibet. He sits down beside Tolstoy in the land of nothing and Nirvana. They are both helpless—one because he must not grasp anything, and the other because he must not let go of anything. The Tolstoyan’s will is frozen by a Buddhist instinct that all special actions are evil. But the Nietzscheite’s will is quite equally frozen by his view that all special actions are good; for if all special actions are good, none of them are special. They stand at the cross-roads, and one hates all the roads and the other likes all the roads. The result is—well, some things are not hard to calculate. They stand at the cross-roads.</Content>
				<Br />
				<Content>Here I end (thank God) the first and dullest business of this book—the rough review of recent thought. After this I begin to sketch a view of life which may not interest my reader, but which, at any rate, interests me. In front of me, as I close this page, is a pile of modern books that I have been turning over for the purpose—a pile of ingenuity, a pile of futility. By the accident of my present detachment, I can see the inevitable smash of the philosophies of Schopenhauer and Tolstoy, Nietzsche and Shaw, as clearly as an inevitable railway smash could be seen from a balloon. They are all on the road to the emptiness of the asylum. For madness may be defined as using mental activity so as to reach mental helplessness; and they have nearly reached it. He who thinks he is made of glass, thinks to the destruction of thought; for glass cannot think. So he who wills to reject nothing, wills the destruction of will; for will is not only the choice of something, but the rejection of almost everything. And as I turn and tumble over the clever, wonderful, tiresome, and useless modern books, the title of one of them rivets my eye. It is called “Jeanne d’Arc,” by Anatole France. I have only glanced at it, but a glance was enough to remind me of Renan’s “Vie de Jésus.” It has the same strange method of the reverent sceptic. It discredits supernatural stories that have some foundation, simply by telling natural stories that have no foundation. Because we cannot believe in what a saint did, we are to pretend that we know exactly what he felt. But I do not mention either book in order to criticise it, but because the accidental combination of the names called up two startling images of sanity which blasted all the books before me. Joan of Arc was not stuck at the cross-roads, either by rejecting all the paths like Tolstoy, or by accepting them all like Nietzsche. She chose a path, and went down it like a thunderbolt. Yet Joan, when I came to think of her, had in her all that was true either in Tolstoy or Nietzsche, all that was even tolerable in either of them. I thought of all that is noble in Tolstoy, the pleasure in plain things, especially in plain pity, the actualities of the earth, the reverence for the poor, the dignity of the bowed back. Joan of Arc had all that and with this great addition, that she endured poverty as well as admiring it; whereas Tolstoy is only a typical aristocrat trying to find out its secret. And then I thought of all that was brave and proud and pathetic in poor Nietzsche, and his mutiny against the emptiness and timidity of our time. I thought of his cry for the ecstatic equilibrium of danger, his hunger for the rush of great horses, his cry to arms. Well, Joan of Arc had all that, and again with this difference, that she did not praise fighting, but fought. We know that she was not afraid of an army, while Nietzsche, for all we know, was afraid of a cow. Tolstoy only praised the peasant; she was the peasant. Nietzsche only praised the warrior; she was the warrior. She beat them both at their own antagonistic ideals; she was more gentle than the one, more violent than the other. Yet she was a perfectly practical person who did something, while they are wild speculators who do nothing. It was impossible that the thought should not cross my mind that she and her faith had perhaps some secret of moral unity and utility that has been lost. And with that thought came a larger one, and the colossal figure of her Master had also crossed the theatre of my thoughts. The same modern difficulty which darkened the subject-matter of Anatole France also darkened that of Ernest Renan. Renan also divided his hero’s pity from his hero’s pugnacity. Renan even represented the righteous anger at Jerusalem as a mere nervous breakdown after the idyllic expectations of Galilee. As if there were any inconsistency between having a love for humanity and having a hatred for inhumanity! Altruists, with thin, weak voices, denounce Christ as an egoist. Egoists (with even thinner and weaker voices) denounce Him as an altruist. In our present atmosphere such cavils are comprehensible enough. The love of a hero is more terrible than the hatred of a tyrant. The hatred of a hero is more generous than the love of a philanthropist. There is a huge and heroic sanity of which moderns can only collect the fragments. There is a giant of whom we see only the lopped arms and legs walking about. They have torn the soul of Christ into silly strips, labelled egoism and altruism, and they are equally puzzled by His insane magnificence and His insane meekness. They have parted His garments among them, and for His vesture they have cast lots; though the coat was without seam woven from the top throughout.</Content>
				<Br />
			</CharacterStyleRange>
		</ParagraphStyleRange>
	</Story>
</Document>
"""