from netrunner.data import mappings


class TestMappings:
    def test_mapping(self):
        assert mappings.FACTION_ASSETS.get("anarch")["glyph_path"] == "NISEI_ANARCH.svg"
