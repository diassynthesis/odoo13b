# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
     

class maj_uniq_partner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [('res_partner_name_uniqu', 'unique(name)', 'Name of partner already exist !')]
#     _sql_constraints = [ ('res_client_name_uniqu', 'unique(name,customer)', 'Ce nom existe déjà !'),    ]
     
#    @api.onchange('name')
#    def _compute_maj_par(self):
#        self.name = self.name.title() if self.name else False

    @api.onchange('name')
    def _compute_maj_par(self):
        # ANCIENNE LOGIQUE COMMENTÉE (Le Saboteur)
        # self.name = self.name.title() if self.name else False
        
        # NOUVELLE DOCTRINE : Différenciation Personne Physique / Société
        if self.name:
            if self.is_company:
                self.name = self.name.upper() # Les Sociétés en MAJUSCULES (ex: SONATRACH -SAIEG)
            else:
                self.name = self.name.title() # Les Individus avec majuscule initiale (ex: Rachid Brahimi - Jean Dupont)
        else:
            self.name = False
            
            
     # =====================================================================
    # AJOUT (Major, session du 27/07/2026) : repéré dans le fork GitHub
    # (soportemegatech/odoo13b), absent de la version Odoo Apps d'origine.
    # Met l'adresse (rue) automatiquement en MAJUSCULES dès sa saisie -
    # convention courante sur les documents officiels/courriers. Purement
    # cosmétique, aucune incidence sur la contrainte d'unicité ni sur la
    # logique Société/Individu ci-dessus.
    # =====================================================================
    @api.onchange('street')
    def _compute_maj_parstreet(self):
        self.street = self.street.upper() if self.street else False        
