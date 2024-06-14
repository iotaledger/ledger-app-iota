use crate::settings::Settings;
use include_gif::include_gif;
use ledger_device_sdk::ui::bagls::Icon;
use ledger_device_sdk::ui::bitmaps::Glyph;
use ledger_prompts_ui::{
    Menu, MenuLabelBottom, MenuLabelTop, BACK_ICON, MENU_ICON_X, MENU_ICON_Y, SETTINGS_ICON,
};

pub const APP_ICON_GLYPH: Glyph = Glyph::from_include(include_gif!("iota-small.gif"));

pub const APP_ICON: Icon = Icon::from(&APP_ICON_GLYPH)
    .set_x(MENU_ICON_X)
    .set_y(MENU_ICON_Y);

pub struct IdleMenuWithSettings {
    pub idle_menu: IdleMenu,
    pub settings: Settings,
}

pub enum IdleMenu {
    AppMain,
    ShowVersion,
    Settings(Option<SettingsSubMenu>),
    Exit,
}

pub enum SettingsSubMenu {
    EnableBlindSigning,
    DisableBlindSigning,
    Back,
}

pub enum BusyMenu {
    Working,
    Cancel,
}

pub struct DoExitApp;

impl Menu for IdleMenuWithSettings {
    type BothResult = DoExitApp;
    fn move_left(&mut self) {
        match self.idle_menu {
            IdleMenu::AppMain => self.idle_menu = IdleMenu::Exit,
            IdleMenu::ShowVersion => self.idle_menu = IdleMenu::AppMain,
            IdleMenu::Settings(None) => self.idle_menu = IdleMenu::ShowVersion,
            IdleMenu::Settings(Some(SettingsSubMenu::Back)) => {
                if self.settings.get() == 1 {
                    self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::DisableBlindSigning))
                } else {
                    self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::EnableBlindSigning))
                }
            }
            IdleMenu::Settings(Some(_)) => {
                self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::Back))
            }
            IdleMenu::Exit => self.idle_menu = IdleMenu::Settings(None),
        };
    }
    fn move_right(&mut self) {
        match self.idle_menu {
            IdleMenu::AppMain => self.idle_menu = IdleMenu::ShowVersion,
            IdleMenu::ShowVersion => self.idle_menu = IdleMenu::Settings(None),
            IdleMenu::Settings(None) => self.idle_menu = IdleMenu::Exit,
            IdleMenu::Settings(Some(SettingsSubMenu::Back)) => {
                if self.settings.get() == 1 {
                    self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::DisableBlindSigning))
                } else {
                    self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::EnableBlindSigning))
                }
            }
            IdleMenu::Settings(Some(_)) => {
                self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::Back))
            }
            IdleMenu::Exit => self.idle_menu = IdleMenu::AppMain,
        };
    }
    #[inline(never)]
    fn handle_both(&mut self) -> Option<Self::BothResult> {
        match self.idle_menu {
            IdleMenu::AppMain => None,
            IdleMenu::ShowVersion => None,
            IdleMenu::Settings(None) => {
                if self.settings.get() == 1 {
                    self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::DisableBlindSigning))
                } else {
                    self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::EnableBlindSigning))
                };
                None
            }
            IdleMenu::Settings(Some(SettingsSubMenu::EnableBlindSigning)) => {
                self.settings.set(&1);
                self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::DisableBlindSigning));
                None
            }
            IdleMenu::Settings(Some(SettingsSubMenu::DisableBlindSigning)) => {
                self.settings.set(&0);
                self.idle_menu = IdleMenu::Settings(Some(SettingsSubMenu::EnableBlindSigning));
                None
            }
            IdleMenu::Settings(Some(SettingsSubMenu::Back)) => {
                self.idle_menu = IdleMenu::Settings(None);
                None
            }
            IdleMenu::Exit => Some(DoExitApp),
        }
    }
    #[inline(never)]
    fn label<'a>(&self) -> (MenuLabelTop<'a>, MenuLabelBottom<'a>) {
        match self.idle_menu {
            IdleMenu::AppMain => (
                MenuLabelTop::Icon(&APP_ICON),
                MenuLabelBottom {
                    text: "IOTA",
                    bold: true,
                },
            ),
            IdleMenu::ShowVersion => (
                MenuLabelTop::Text("Version"),
                MenuLabelBottom {
                    text: env!("CARGO_PKG_VERSION"),
                    bold: false,
                },
            ),
            IdleMenu::Settings(None) => (
                MenuLabelTop::Icon(&SETTINGS_ICON),
                MenuLabelBottom {
                    text: "Settings",
                    bold: true,
                },
            ),
            IdleMenu::Settings(Some(SettingsSubMenu::EnableBlindSigning)) => (
                MenuLabelTop::Text("Blind Signing"),
                MenuLabelBottom {
                    text: "Disabled",
                    bold: false,
                },
            ),
            IdleMenu::Settings(Some(SettingsSubMenu::DisableBlindSigning)) => (
                MenuLabelTop::Text("Blind Signing"),
                MenuLabelBottom {
                    text: "Enabled",
                    bold: false,
                },
            ),
            IdleMenu::Settings(Some(SettingsSubMenu::Back)) => (
                MenuLabelTop::Icon(&BACK_ICON),
                MenuLabelBottom {
                    text: "Back",
                    bold: true,
                },
            ),
            IdleMenu::Exit => (
                MenuLabelTop::Icon(&ledger_prompts_ui::DASHBOARD_ICON),
                MenuLabelBottom {
                    text: "Quit",
                    bold: true,
                },
            ),
        }
    }
}

pub struct DoCancel;

impl Menu for BusyMenu {
    type BothResult = DoCancel;
    fn move_left(&mut self) {
        *self = BusyMenu::Working;
    }
    fn move_right(&mut self) {
        *self = BusyMenu::Cancel;
    }
    #[inline(never)]
    fn handle_both(&mut self) -> Option<Self::BothResult> {
        match self {
            BusyMenu::Working => None,
            BusyMenu::Cancel => Some(DoCancel),
        }
    }
    #[inline(never)]
    fn label<'a>(&self) -> (MenuLabelTop<'a>, MenuLabelBottom<'a>) {
        match self {
            BusyMenu::Working => (
                MenuLabelTop::Text("Working..."),
                MenuLabelBottom {
                    text: "",
                    bold: false,
                },
            ),
            BusyMenu::Cancel => (
                MenuLabelTop::Text("Cancel"),
                MenuLabelBottom {
                    text: "",
                    bold: false,
                },
            ),
        }
    }
}
