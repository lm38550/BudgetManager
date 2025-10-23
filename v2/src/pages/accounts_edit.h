#pragma once
#include "../models/dataAcces.h"
#include <wx/listctrl.h>
#include <wx/wx.h>

class AccountsEdit : public wxFrame {
public:
    AccountsEdit(wxWindow* parent);
private:
    dataAcces DA;
    auto FullfilList(wxPanel* panel);
    void LoadDisplay();
};
