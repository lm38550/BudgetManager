#include "accounts_edit.h"
#include <vector>
#include <string>
#include <wx/gbsizer.h>
#include <wx/panel.h>

dataAcces DA;

enum {
    ID_list = 2001,
    ID_label = 2002,
    ID_button_up = 2003,
    ID_button_supp = 2004,
    ID_button_down = 2005,
    ID_button_add = 2006
};

AccountsEdit::AccountsEdit(wxWindow* parent)
    : wxFrame(parent, wxID_ANY, "Gestion des comptes", wxDefaultPosition, wxSize(300, 200))
{
    
    // Charge la page
    LoadDisplay();

}

auto AccountsEdit::FullfilList(wxPanel* panel) {

    // Créé une nouvelle liste
    auto list_accounts = new wxListCtrl(panel, ID_list, wxDefaultPosition,
                                        wxSize(300,200),
                                        wxLC_REPORT | wxLC_SINGLE_SEL);

    // Ajout d'une colonne
    list_accounts->InsertColumn(0, "Nom du compte", wxLIST_FORMAT_LEFT);

    // Récupère les comptes dans la base de donnée
    vector<int> a;
    vector<string> name_accounts;
    vector<float> b;
    DA.getAccountList(a, name_accounts, b);

    // Rempli la liste
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

    // Place la liste
    auto AccountsList = FullfilList(panel);
    sizer->Add(AccountsList, {0,0}, {5,1}, wxEXPAND);
    
    // Place le label de création de compte
    auto TextLabel = new wxTextCtrl(panel,ID_label);
    sizer->Add(TextLabel, {5,0}, {1,1}, wxEXPAND);

    // Place le bouton UP
    auto UpButton = new wxButton(panel, ID_button_up, "/\\");
    sizer->Add(UpButton, {1,1}, {1,1}, wxEXPAND);

    // Place le bouton Supprimer
    auto SuppButton = new wxButton(panel, ID_button_supp, "Supprimer");
    sizer->Add(SuppButton, {2,1}, {1,1}, wxEXPAND);

    // Place le bouton DOWN
    auto DownButton = new wxButton(panel, ID_button_down, "\\/");
    sizer->Add(DownButton, {3,1}, {1,1}, wxEXPAND);

    // Place le bouton Ajouter
    auto AddButton = new wxButton(panel, ID_button_add, "Ajouter");
    sizer->Add(AddButton, {5,1}, {1,1}, wxEXPAND);


    // Défini les colonnes pouvant se redimentionner
    sizer->AddGrowableCol(0);

    // Défini les lignes pouvant se redimentionner
    sizer->AddGrowableRow(0);
    sizer->AddGrowableRow(4);

    // Ajoute à l'affichage
    panel->SetSizer(sizer);
    mainSizer->Add(panel, 1, wxEXPAND | wxALL, margin);
    this->SetSizerAndFit(mainSizer);
}
