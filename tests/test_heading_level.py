import sublime

from MarkdownEditing.tests import DereferrablePanelTestCase


class ChangeHeadingLevelTestCase(DereferrablePanelTestCase):

    def test_increase_open_heading1_6_level_by(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", False)
        self.setText("heading")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("# heading")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("## heading")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("### heading")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("#### heading")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("##### heading")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("###### heading")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("heading")

    def test_increase_closed_heading1_6_level_by(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", True)
        self.setText("heading")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("# heading #")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("## heading ##")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("### heading ###")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("#### heading ####")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("##### heading #####")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("###### heading ######")

        self.view.run_command("mde_change_headings_level", {"by": 1})
        self.assertEqualText("heading")

    def test_decrease_open_heading1_6_level_by(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", False)
        self.setText("heading")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("###### heading")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("##### heading")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("#### heading")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("### heading")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("## heading")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("# heading")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("heading")

    def test_decrease_open_heading7_level_by(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", False)
        self.setText("####### heading")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("###### heading")

    def test_decrease_open_heading8_level_by(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", False)
        self.setText("######## heading")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("heading")

    def test_decrease_closed_heading1_6_level_by(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", True)
        self.setText("heading")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("###### heading ######")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("##### heading #####")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("#### heading ####")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("### heading ###")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("## heading ##")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("# heading #")

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("heading")

    def test_decrease_closed_heading7_level_by(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", True)
        self.setText("####### heading #######")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("###### heading ######")

    def test_decrease_closed_heading8_level_by(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", True)
        self.setText("####### heading #######")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"by": -1})
        self.assertEqualText("###### heading ######")

    def test_set_open_heading_level_to(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", False)
        self.setText("heading")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"to": 1})
        self.assertEqualText("# heading")

        self.view.run_command("mde_change_headings_level", {"to": 2})
        self.assertEqualText("## heading")

        self.view.run_command("mde_change_headings_level", {"to": 3})
        self.assertEqualText("### heading")

        self.view.run_command("mde_change_headings_level", {"to": 4})
        self.assertEqualText("#### heading")

        self.view.run_command("mde_change_headings_level", {"to": 5})
        self.assertEqualText("##### heading")

        self.view.run_command("mde_change_headings_level", {"to": 6})
        self.assertEqualText("###### heading")

        self.view.run_command("mde_change_headings_level", {"to": 0})
        self.assertEqualText("heading")

    def test_set_closed_heading_level_to(self):
        self.view.settings().set("mde.detect_heading_style", False)
        self.view.settings().set("mde.match_heading_hashes", True)
        self.setText("heading")
        self.setCaretTo(1, 1)

        self.view.run_command("mde_change_headings_level", {"to": 1})
        self.assertEqualText("# heading #")

        self.view.run_command("mde_change_headings_level", {"to": 2})
        self.assertEqualText("## heading ##")

        self.view.run_command("mde_change_headings_level", {"to": 3})
        self.assertEqualText("### heading ###")

        self.view.run_command("mde_change_headings_level", {"to": 4})
        self.assertEqualText("#### heading ####")

        self.view.run_command("mde_change_headings_level", {"to": 5})
        self.assertEqualText("##### heading #####")

        self.view.run_command("mde_change_headings_level", {"to": 6})
        self.assertEqualText("###### heading ######")

        self.view.run_command("mde_change_headings_level", {"to": 0})
        self.assertEqualText("heading")
