#include "accounts_edit.h"
#include "../dataAcces.h"
#include <wx/wx.h>
#include <wx/listctrl.h>
#include <vector>
#include <string>
#include <wx/gbsizer.h>
#include <wx/panel.h>

AccountsEdit::AccountsEdit(wxWindow* parent)
    : wxFrame(parent, wxID_ANY, "Deuxième page", wxDefaultPosition, wxSize(300, 200))
{
    new wxStaticText(this, wxID_ANY, "Bienvenue sur la deuxième page !", 
                     wxPoint(20, 20));



    const auto margin = FromDIP(10);

    auto mainSizer = new wxBoxSizer(wxVERTICAL);
    wxPanel *panel = new wxPanel(this, wxID_ANY);

    auto sizer = new wxGridBagSizer(margin, margin);

    vector<pair<wxGBPosition,wxGBSpan>> items = {
            {{0,0},{5,1}},
            {{5,0},{1,1}},
            {{0,1},{1,1}},
            {{1,1},{1,1}},
            {{2,1},{1,1}},
            {{3,1},{1,1}},
            {{4,1},{1,1}},
            {{5,1},{1,1}}};

    for (auto &item : items) {
        auto initialSize = sizer->GetEmptyCellSize() * 2;

        if (item.first == wxGBPosition(1,1)) {
            initialSize.SetWidth(FromDIP(150));
        }
        if (item.first == wxGBPosition(0,0)) {
            initialSize.SetWidth(FromDIP(250));
        }

        auto p = new wxPanel(panel, wxID_ANY, wxDefaultPosition, initialSize);
        p->SetBackgroundColour(wxColour(100, 100, 200));

        sizer->Add(p, item.first, item.second, wxEXPAND);
    }

    sizer->AddGrowableCol(0);

    sizer->AddGrowableRow(0);
    sizer->AddGrowableRow(4);

    panel->SetSizer(sizer);

    mainSizer->Add(panel, 1, wxEXPAND | wxALL, margin);
    this->SetSizerAndFit(mainSizer);


    /* PARTIE DE CREATION DE LISTE

    wxListCtrl* list_accounts = new wxListCtrl(this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 
                                              wxLC_REPORT | wxLC_SINGLE_SEL);

    // Ajout d'une colonne
        list_accounts->InsertColumn(0, "Nom", wxLIST_FORMAT_LEFT, 200);

    dataAcces DA;

    vector<int> a;
    vector<string> name_accounts;
    vector<float> b;

    DA.getAccountList(a,name_accounts,b);

    long index = 0;
        for (const auto& nom : name_accounts) {
            list_accounts->InsertItem(index, nom);
            index++;
        }

    */

}


