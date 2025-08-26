#include "accounts_edit.h"
#include <vector>
#include <string>
#include <wx/gbsizer.h>
#include <wx/panel.h>

dataAcces DA;

AccountsEdit::AccountsEdit(wxWindow* parent)
    : wxFrame(parent, wxID_ANY, "Gestion des comptes", wxDefaultPosition, wxSize(300, 200))
{
    
    LoadDisplay();

}

auto AccountsEdit::FullfilList(wxPanel* panel) {

    auto list_accounts = new wxListCtrl(panel, wxID_ANY, wxDefaultPosition,
                                        wxSize(300,200),
                                        wxLC_REPORT | wxLC_SINGLE_SEL);

    // Ajout d'une colonne
    list_accounts->InsertColumn(0, "Nom du compte", wxLIST_FORMAT_LEFT);

    vector<int> a;
    vector<string> name_accounts;
    vector<float> b;

    DA.getAccountList(a, name_accounts, b);

    long index = 0;
    for (const auto& nom : name_accounts) {
        list_accounts->InsertItem(index, nom);
        index++;
    }

    // Ajustement dynamique lors du resize
    list_accounts->Bind(wxEVT_SIZE, [list_accounts](wxSizeEvent& event) {
        int totalWidth = list_accounts->GetClientSize().GetWidth();
        list_accounts->SetColumnWidth(0, totalWidth - 4); // -4 pour éviter la barre de scroll
        event.Skip();
    });

    // Initialisation de la largeur
    list_accounts->SetColumnWidth(0, list_accounts->GetClientSize().GetWidth() - 4);

    return list_accounts;
}


void AccountsEdit::LoadDisplay() {
    const auto margin = FromDIP(10);

    auto mainSizer = new wxBoxSizer(wxVERTICAL);
    wxPanel *panel = new wxPanel(this, wxID_ANY);

    auto sizer = new wxGridBagSizer(margin, margin);

    sizer->Add(FullfilList(panel), {0,0}, {5,1}, wxEXPAND);
    
    auto TextLabel = new wxTextCtrl(panel,wxID_ANY);
    sizer->Add(TextLabel, {5,0}, {1,1}, wxEXPAND);

    auto UpButton = new wxButton(panel, wxID_ANY, "/\\");
    sizer->Add(UpButton, {1,1}, {1,1}, wxEXPAND);

    auto SuppButton = new wxButton(panel, wxID_ANY, "Supprimer");
    sizer->Add(SuppButton, {2,1}, {1,1}, wxEXPAND);

    auto DownButton = new wxButton(panel, wxID_ANY, "\\/");
    sizer->Add(DownButton, {3,1}, {1,1}, wxEXPAND);

    auto AddButton = new wxButton(panel, wxID_ANY, "Ajouter");
    sizer->Add(AddButton, {5,1}, {1,1}, wxEXPAND);


    sizer->AddGrowableCol(0);

    sizer->AddGrowableRow(0);
    sizer->AddGrowableRow(4);

    panel->SetSizer(sizer);

    mainSizer->Add(panel, 1, wxEXPAND | wxALL, margin);
    this->SetSizerAndFit(mainSizer);
}
