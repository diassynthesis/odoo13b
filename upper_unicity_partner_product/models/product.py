# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class product_template_inherit(models.Model):
    _inherit = 'product.template'
     
    _sql_constraints = [('product_template_name_uniqu', 'unique(name)', 'Product already exist!')]
     
    @api.onchange('name')
    def _compute_maj_temp(self):
#        self.name = self.name.title() if self.name else False
        self.name = self.name.upper() if self.name else False
        
class product_pro_inherit(models.Model):
    _inherit = 'product.product'
    
    # =====================================================================
    # CORRECTIF (session du 27/07/2026) : product.product n'a AUCUNE
    # colonne 'name' physique en base dans Odoo 13 (confirmé par
    # information_schema.columns - name est un champ related vers
    # product.template.name, jamais stocké ici). Cette contrainte ne
    # pourra donc jamais être créée, d'où l'erreur répétée à chaque
    # mise à jour de module ("unable to add constraint... unique(name)").
    # Commentée plutôt que supprimée - la contrainte équivalente sur
    # product.template (fichier product_template_inherit ci-dessus)
    # reste intacte et suffit à garantir l'unicité des noms de produits.
    #
    # ANCIEN (conservé) :
    # _sql_constraints = [('product_product_name_uniqu', 'unique(name)', 'Product already exist!')]
    # =====================================================================
     
#    _sql_constraints = [('product_product_name_uniqu', 'unique(name)', 'Product already exist!')]

    @api.onchange('name')
    def _compute_maj_pro(self):
#        self.name = self.name.title() if self.name else False
        self.name = self.name.upper() if self.name else False
        
