# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ArchPath",
    "author" : "Your Name", 
    "description" : "",
    "blender" : (4, 2, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews
from hbim_open_api_client import Client, types

client = Client()

addon_keymaps = {}
_icons = None
preferences = {'sna_connection_status': 'not connected', }


def sna_update_sna_pr_diagnostico_id_cadastro_9275B(self, context):
    sna_updated_prop = self.sna_pr_diagnostico_id_cadastro


class SNA_OT_Archpath_Op_Connect_19B86(bpy.types.Operator):
    bl_idname = "sna.archpath_op_connect_19b86"
    bl_label = "ARCHPATH_OP_CONNECT"
    bl_description = "connect to server"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        global client
        client = Client(base_url=bpy.types.Scene.sna_pr_url)
        client._base_url
        bpy.context.scene.sna_pr_connection_status = 'Successfully connected!, client._base_url'
        print(bpy.context.scene.sna_pr_connection_status)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Archpath_Op_Disconnect_783Ee(bpy.types.Operator):
    bl_idname = "sna.archpath_op_disconnect_783ee"
    bl_label = "ARCHPATH_OP_DISCONNECT"
    bl_description = "connect to server"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        global client
        bpy.context.scene.sna_pr_connection_status = 'disconnected'
        
        print(bpy.context.scene.sna_pr_connection_status)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Archpath_Op_Edificacao_Post_940Dc(bpy.types.Operator):
    bl_idname = "sna.archpath_op_edificacao_post_940dc"
    bl_label = "ARCHPATH_OP_EDIFICACAO_POST"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        print(bpy.context.scene.sna_pr_edf_nome, bpy.context.scene.sna_pr_edf_descricao_historica)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_CADASTRAR__EDIFICAO_B585A(bpy.types.Panel):
    bl_label = 'Cadastrar - Edificação'
    bl_idname = 'SNA_PT_CADASTRAR__EDIFICAO_B585A'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_08E77 = layout.box()
        box_08E77.alert = False
        box_08E77.enabled = True
        box_08E77.active = True
        box_08E77.use_property_split = False
        box_08E77.use_property_decorate = False
        box_08E77.alignment = 'Expand'.upper()
        box_08E77.scale_x = 1.0
        box_08E77.scale_y = 1.0
        if not True: box_08E77.operator_context = "EXEC_DEFAULT"
        col_49DE4 = box_08E77.column(heading='', align=False)
        col_49DE4.alert = False
        col_49DE4.enabled = True
        col_49DE4.active = True
        col_49DE4.use_property_split = False
        col_49DE4.use_property_decorate = False
        col_49DE4.scale_x = 1.0
        col_49DE4.scale_y = 1.0
        col_49DE4.alignment = 'Expand'.upper()
        col_49DE4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_49DE4.prop(bpy.context.scene, 'sna_pr_edf_nome', text='Nome', icon_value=0, emboss=True)
        col_49DE4.prop(bpy.context.scene, 'sna_pr_edf_data_construcao', text='Data de Construção', icon_value=0, emboss=True)
        col_49DE4.prop(bpy.context.scene, 'sna_pr_edf_nome', text='Valor Patrimonial', icon_value=0, emboss=True)
        col_49DE4.prop(bpy.context.scene, 'sna_pr_edf_descricao_historica', text='Descriçao Histórica', icon_value=0, emboss=True)
        op = col_49DE4.operator('sna.archpath_op_edificacao_post_940dc', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_CADASTRAR__USURIO_2CEF3(bpy.types.Panel):
    bl_label = 'Cadastrar - Usuário'
    bl_idname = 'SNA_PT_CADASTRAR__USURIO_2CEF3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_91591 = layout.box()
        box_91591.alert = False
        box_91591.enabled = True
        box_91591.active = True
        box_91591.use_property_split = False
        box_91591.use_property_decorate = False
        box_91591.alignment = 'Expand'.upper()
        box_91591.scale_x = 1.0
        box_91591.scale_y = 1.0
        if not True: box_91591.operator_context = "EXEC_DEFAULT"
        col_2F5F5 = box_91591.column(heading='', align=False)
        col_2F5F5.alert = False
        col_2F5F5.enabled = True
        col_2F5F5.active = True
        col_2F5F5.use_property_split = False
        col_2F5F5.use_property_decorate = False
        col_2F5F5.scale_x = 1.0
        col_2F5F5.scale_y = 1.0
        col_2F5F5.alignment = 'Expand'.upper()
        col_2F5F5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_2F5F5.prop(bpy.context.scene, 'sna_pr_user_nome', text='Nome', icon_value=0, emboss=True)
        col_2F5F5.prop(bpy.context.scene, 'sna_pr_username', text='Username', icon_value=0, emboss=True)
        col_2F5F5.prop(bpy.context.scene, 'sna_pr_user_email', text='Email', icon_value=0, emboss=True)
        col_2F5F5.prop(bpy.context.scene, 'sna_pr_password', text='Password', icon_value=0, emboss=True)
        col_2F5F5.prop(bpy.context.scene, 'sna_pr_user_formacao', text='Formação Acadêmica', icon_value=0, emboss=True)
        col_2F5F5.prop(bpy.context.scene, 'sna_pr_user_data_nascimento', text='Data de Nascimento', icon_value=0, emboss=True)
        op = col_2F5F5.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_CADASTRAR__CADASTRO_ARQUITETNICO_9722D(bpy.types.Panel):
    bl_label = 'Cadastrar - Cadastro Arquitetônico'
    bl_idname = 'SNA_PT_CADASTRAR__CADASTRO_ARQUITETNICO_9722D'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_D1FF4 = layout.box()
        box_D1FF4.alert = False
        box_D1FF4.enabled = True
        box_D1FF4.active = True
        box_D1FF4.use_property_split = False
        box_D1FF4.use_property_decorate = False
        box_D1FF4.alignment = 'Expand'.upper()
        box_D1FF4.scale_x = 1.0
        box_D1FF4.scale_y = 1.0
        if not True: box_D1FF4.operator_context = "EXEC_DEFAULT"
        col_D06BF = box_D1FF4.column(heading='', align=False)
        col_D06BF.alert = False
        col_D06BF.enabled = True
        col_D06BF.active = True
        col_D06BF.use_property_split = False
        col_D06BF.use_property_decorate = False
        col_D06BF.scale_x = 1.0
        col_D06BF.scale_y = 1.0
        col_D06BF.alignment = 'Expand'.upper()
        col_D06BF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_D06BF.prop(bpy.context.scene, 'sna_pr_cadastro_id_edificacao', text='ID da Edificação', icon_value=0, emboss=True)
        col_D06BF.prop(bpy.context.scene, 'sna_pr_cadastro_id_user', text='ID do Usuário', icon_value=0, emboss=True)
        col_D06BF.prop(bpy.context.scene, 'sna_pr_cadastro_data', text='Data de Cadastro', icon_value=0, emboss=True)
        col_D06BF.prop(bpy.context.scene, 'sna_pr_cadastro_responsavel_tecnico', text='Responsável Técnico', icon_value=0, emboss=True)
        col_D06BF.prop(bpy.context.scene, 'sna_pr_cadastro_id_arquivo', text='ID do Arquivo', icon_value=0, emboss=True)
        op = col_D06BF.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_CADASTRAR__DIAGNSTICO_DANO_F7238(bpy.types.Panel):
    bl_label = 'Cadastrar - Diagnóstico Dano'
    bl_idname = 'SNA_PT_CADASTRAR__DIAGNSTICO_DANO_F7238'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_C6C3B = layout.box()
        box_C6C3B.alert = False
        box_C6C3B.enabled = True
        box_C6C3B.active = True
        box_C6C3B.use_property_split = False
        box_C6C3B.use_property_decorate = False
        box_C6C3B.alignment = 'Expand'.upper()
        box_C6C3B.scale_x = 1.0
        box_C6C3B.scale_y = 1.0
        if not True: box_C6C3B.operator_context = "EXEC_DEFAULT"
        col_07BF5 = box_C6C3B.column(heading='', align=False)
        col_07BF5.alert = False
        col_07BF5.enabled = True
        col_07BF5.active = True
        col_07BF5.use_property_split = False
        col_07BF5.use_property_decorate = False
        col_07BF5.scale_x = 1.0
        col_07BF5.scale_y = 1.0
        col_07BF5.alignment = 'Expand'.upper()
        col_07BF5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_07BF5.prop(bpy.context.scene, 'sna_pr_diagnostico_nome', text='Nome do Dano:', icon_value=0, emboss=True)
        col_07BF5.prop(bpy.context.scene, 'sna_pr_diagnostico_agente_dano', text='Agente(s)', icon_value=0, emboss=True)
        col_07BF5.prop(bpy.context.scene, 'sna_pr_diagnostico_descricao_causa', text='Possíveis Causas', icon_value=0, emboss=True)
        col_07BF5.prop(bpy.context.scene, 'sna_pr_diagnostico_relacao_elem_const', text='Elemento de construçao associado(s)', icon_value=0, emboss=True)
        col_07BF5.prop(bpy.context.scene, 'sna_pr_diagnostico_id_cadastro', text='ID do Cadastro relacionado', icon_value=0, emboss=True)
        col_07BF5.prop(bpy.context.scene, 'sna_pr_diagnostico_id_tipo_dano', text='ID do Tipo do Dano', icon_value=0, emboss=True)
        col_07BF5.prop(bpy.context.scene, 'sna_pr_diagnostico_geometria', text='ID Geometria do Elemento', icon_value=0, emboss=True)
        col_07BF5.prop(bpy.context.scene, 'sna_pr_diagnostico_id_arquivo', text='ID dos Arquivo Associados.', icon_value=0, emboss=True)
        op = col_07BF5.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_CADASTRAR__GEOMETRIA_DANO_5C854(bpy.types.Panel):
    bl_label = 'Cadastrar - Geometria Dano'
    bl_idname = 'SNA_PT_CADASTRAR__GEOMETRIA_DANO_5C854'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_0C5B8 = layout.box()
        box_0C5B8.alert = False
        box_0C5B8.enabled = True
        box_0C5B8.active = True
        box_0C5B8.use_property_split = False
        box_0C5B8.use_property_decorate = False
        box_0C5B8.alignment = 'Expand'.upper()
        box_0C5B8.scale_x = 1.0
        box_0C5B8.scale_y = 1.0
        if not True: box_0C5B8.operator_context = "EXEC_DEFAULT"
        col_20B7C = box_0C5B8.column(heading='', align=False)
        col_20B7C.alert = False
        col_20B7C.enabled = True
        col_20B7C.active = True
        col_20B7C.use_property_split = False
        col_20B7C.use_property_decorate = False
        col_20B7C.scale_x = 1.0
        col_20B7C.scale_y = 1.0
        col_20B7C.alignment = 'Expand'.upper()
        col_20B7C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_20B7C.prop(bpy.context.scene, 'sna_pr_geometria_global_id_ifc', text='Global ID IFC', icon_value=0, emboss=True)
        col_20B7C.prop(bpy.context.scene, 'sna_pr_geometria_id_arquivo', text='ID do Arquivo correspondente', icon_value=0, emboss=True)
        op = col_20B7C.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_INSERIR__ARQUIVO_8D1E0(bpy.types.Panel):
    bl_label = 'Inserir - Arquivo'
    bl_idname = 'SNA_PT_INSERIR__ARQUIVO_8D1E0'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_0BEC9 = layout.box()
        box_0BEC9.alert = False
        box_0BEC9.enabled = True
        box_0BEC9.active = True
        box_0BEC9.use_property_split = False
        box_0BEC9.use_property_decorate = False
        box_0BEC9.alignment = 'Expand'.upper()
        box_0BEC9.scale_x = 1.0
        box_0BEC9.scale_y = 1.0
        if not True: box_0BEC9.operator_context = "EXEC_DEFAULT"
        col_02367 = box_0BEC9.column(heading='', align=False)
        col_02367.alert = False
        col_02367.enabled = True
        col_02367.active = True
        col_02367.use_property_split = False
        col_02367.use_property_decorate = False
        col_02367.scale_x = 1.0
        col_02367.scale_y = 1.0
        col_02367.alignment = 'Expand'.upper()
        col_02367.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_02367.prop(bpy.context.scene, 'sna_pr_bin_file_filename', text='Nome', icon_value=0, emboss=True)
        col_02367.prop(bpy.context.scene, 'sna_pr_bin_file_content', text='Inserir', icon_value=0, emboss=True)
        op = col_02367.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_PESQUISAR__EDIFICAO_09595(bpy.types.Panel):
    bl_label = 'Pesquisar - Edificação'
    bl_idname = 'SNA_PT_PESQUISAR__EDIFICAO_09595'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_A5378 = layout.box()
        box_A5378.alert = False
        box_A5378.enabled = True
        box_A5378.active = True
        box_A5378.use_property_split = False
        box_A5378.use_property_decorate = False
        box_A5378.alignment = 'Expand'.upper()
        box_A5378.scale_x = 1.0
        box_A5378.scale_y = 1.0
        if not True: box_A5378.operator_context = "EXEC_DEFAULT"
        col_8F430 = box_A5378.column(heading='', align=False)
        col_8F430.alert = False
        col_8F430.enabled = True
        col_8F430.active = True
        col_8F430.use_property_split = False
        col_8F430.use_property_decorate = False
        col_8F430.scale_x = 1.0
        col_8F430.scale_y = 1.0
        col_8F430.alignment = 'Expand'.upper()
        col_8F430.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_8F430.prop(bpy.context.scene, 'sna_pr_edf_id', text='ID Edificação', icon_value=0, emboss=True)
        op = col_8F430.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_PESQUISAR_USURIO_E4B88(bpy.types.Panel):
    bl_label = 'Pesquisar- Usuário'
    bl_idname = 'SNA_PT_PESQUISAR_USURIO_E4B88'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_A7522 = layout.box()
        box_A7522.alert = False
        box_A7522.enabled = True
        box_A7522.active = True
        box_A7522.use_property_split = False
        box_A7522.use_property_decorate = False
        box_A7522.alignment = 'Expand'.upper()
        box_A7522.scale_x = 1.0
        box_A7522.scale_y = 1.0
        if not True: box_A7522.operator_context = "EXEC_DEFAULT"
        col_518DA = box_A7522.column(heading='', align=False)
        col_518DA.alert = False
        col_518DA.enabled = True
        col_518DA.active = True
        col_518DA.use_property_split = False
        col_518DA.use_property_decorate = False
        col_518DA.scale_x = 1.0
        col_518DA.scale_y = 1.0
        col_518DA.alignment = 'Expand'.upper()
        col_518DA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_518DA.prop(bpy.context.scene, 'sna_pr_userid', text='ID do Usuário', icon_value=0, emboss=True)
        op = col_518DA.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_PESQUISAR_CADASTRO_ARQUITETNICO_D2668(bpy.types.Panel):
    bl_label = 'Pesquisar- Cadastro Arquitetônico'
    bl_idname = 'SNA_PT_PESQUISAR_CADASTRO_ARQUITETNICO_D2668'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_4A9D2 = layout.box()
        box_4A9D2.alert = False
        box_4A9D2.enabled = True
        box_4A9D2.active = True
        box_4A9D2.use_property_split = False
        box_4A9D2.use_property_decorate = False
        box_4A9D2.alignment = 'Expand'.upper()
        box_4A9D2.scale_x = 1.0
        box_4A9D2.scale_y = 1.0
        if not True: box_4A9D2.operator_context = "EXEC_DEFAULT"
        col_A9CE4 = box_4A9D2.column(heading='', align=False)
        col_A9CE4.alert = False
        col_A9CE4.enabled = True
        col_A9CE4.active = True
        col_A9CE4.use_property_split = False
        col_A9CE4.use_property_decorate = False
        col_A9CE4.scale_x = 1.0
        col_A9CE4.scale_y = 1.0
        col_A9CE4.alignment = 'Expand'.upper()
        col_A9CE4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_A9CE4.prop(bpy.context.scene, 'sna_pr_cadastro_id', text='ID do Cadastro Arquitetônico', icon_value=0, emboss=True)
        op = col_A9CE4.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_PESQUISAR__DIAGNSTICO_DANO_32B58(bpy.types.Panel):
    bl_label = 'Pesquisar - Diagnóstico Dano'
    bl_idname = 'SNA_PT_PESQUISAR__DIAGNSTICO_DANO_32B58'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_C9969 = layout.box()
        box_C9969.alert = False
        box_C9969.enabled = True
        box_C9969.active = True
        box_C9969.use_property_split = False
        box_C9969.use_property_decorate = False
        box_C9969.alignment = 'Expand'.upper()
        box_C9969.scale_x = 1.0
        box_C9969.scale_y = 1.0
        if not True: box_C9969.operator_context = "EXEC_DEFAULT"
        col_2D581 = box_C9969.column(heading='', align=False)
        col_2D581.alert = False
        col_2D581.enabled = True
        col_2D581.active = True
        col_2D581.use_property_split = False
        col_2D581.use_property_decorate = False
        col_2D581.scale_x = 1.0
        col_2D581.scale_y = 1.0
        col_2D581.alignment = 'Expand'.upper()
        col_2D581.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_2D581.prop(bpy.context.scene, 'sna_pr_diagnostico_id', text='ID do Diagnóstico', icon_value=0, emboss=True)
        op = col_2D581.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_PESQUISAR__GEOMETRIA_DANO_079E6(bpy.types.Panel):
    bl_label = 'Pesquisar - Geometria Dano'
    bl_idname = 'SNA_PT_PESQUISAR__GEOMETRIA_DANO_079E6'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_7C699 = layout.box()
        box_7C699.alert = False
        box_7C699.enabled = True
        box_7C699.active = True
        box_7C699.use_property_split = False
        box_7C699.use_property_decorate = False
        box_7C699.alignment = 'Expand'.upper()
        box_7C699.scale_x = 1.0
        box_7C699.scale_y = 1.0
        if not True: box_7C699.operator_context = "EXEC_DEFAULT"
        col_C2732 = box_7C699.column(heading='', align=False)
        col_C2732.alert = False
        col_C2732.enabled = True
        col_C2732.active = True
        col_C2732.use_property_split = False
        col_C2732.use_property_decorate = False
        col_C2732.scale_x = 1.0
        col_C2732.scale_y = 1.0
        col_C2732.alignment = 'Expand'.upper()
        col_C2732.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_C2732.prop(bpy.context.scene, 'sna_pr_geometria_id', text='ID da Geometria', icon_value=0, emboss=True)
        op = col_C2732.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_DOWNLOAD__ARQUIVOS_4E3A0(bpy.types.Panel):
    bl_label = 'Download - Arquivo(s)'
    bl_idname = 'SNA_PT_DOWNLOAD__ARQUIVOS_4E3A0'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_E021C = layout.box()
        box_E021C.alert = False
        box_E021C.enabled = True
        box_E021C.active = True
        box_E021C.use_property_split = False
        box_E021C.use_property_decorate = False
        box_E021C.alignment = 'Expand'.upper()
        box_E021C.scale_x = 1.0
        box_E021C.scale_y = 1.0
        if not True: box_E021C.operator_context = "EXEC_DEFAULT"
        col_F634E = box_E021C.column(heading='', align=False)
        col_F634E.alert = False
        col_F634E.enabled = True
        col_F634E.active = True
        col_F634E.use_property_split = False
        col_F634E.use_property_decorate = False
        col_F634E.scale_x = 1.0
        col_F634E.scale_y = 1.0
        col_F634E.alignment = 'Expand'.upper()
        col_F634E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_F634E.prop(bpy.context.scene, 'sna_pr_bin_file_id_download', text='File ID', icon_value=0, emboss=True)
        op = col_F634E.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EXCLUIR__EDIFICAO_2E503(bpy.types.Panel):
    bl_label = 'Excluir - Edificação'
    bl_idname = 'SNA_PT_EXCLUIR__EDIFICAO_2E503'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_8C5CB = layout.box()
        box_8C5CB.alert = False
        box_8C5CB.enabled = True
        box_8C5CB.active = True
        box_8C5CB.use_property_split = False
        box_8C5CB.use_property_decorate = False
        box_8C5CB.alignment = 'Expand'.upper()
        box_8C5CB.scale_x = 1.0
        box_8C5CB.scale_y = 1.0
        if not True: box_8C5CB.operator_context = "EXEC_DEFAULT"
        col_77E50 = box_8C5CB.column(heading='', align=False)
        col_77E50.alert = False
        col_77E50.enabled = True
        col_77E50.active = True
        col_77E50.use_property_split = False
        col_77E50.use_property_decorate = False
        col_77E50.scale_x = 1.0
        col_77E50.scale_y = 1.0
        col_77E50.alignment = 'Expand'.upper()
        col_77E50.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_77E50.prop(bpy.context.scene, 'sna_pr_edf_id', text='ID Edificação', icon_value=0, emboss=True)
        op = col_77E50.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EXCLUIR__USURIO_39D2E(bpy.types.Panel):
    bl_label = 'Excluir - Usuário'
    bl_idname = 'SNA_PT_EXCLUIR__USURIO_39D2E'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_7D635 = layout.box()
        box_7D635.alert = False
        box_7D635.enabled = True
        box_7D635.active = True
        box_7D635.use_property_split = False
        box_7D635.use_property_decorate = False
        box_7D635.alignment = 'Expand'.upper()
        box_7D635.scale_x = 1.0
        box_7D635.scale_y = 1.0
        if not True: box_7D635.operator_context = "EXEC_DEFAULT"
        col_5ADE2 = box_7D635.column(heading='', align=False)
        col_5ADE2.alert = False
        col_5ADE2.enabled = True
        col_5ADE2.active = True
        col_5ADE2.use_property_split = False
        col_5ADE2.use_property_decorate = False
        col_5ADE2.scale_x = 1.0
        col_5ADE2.scale_y = 1.0
        col_5ADE2.alignment = 'Expand'.upper()
        col_5ADE2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_5ADE2.prop(bpy.context.scene, 'sna_pr_userid', text='ID do Usuário', icon_value=0, emboss=True)
        op = col_5ADE2.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EXCLUIR__CADASTRO_ARQUITETNICO_1954D(bpy.types.Panel):
    bl_label = 'Excluir - Cadastro Arquitetônico'
    bl_idname = 'SNA_PT_EXCLUIR__CADASTRO_ARQUITETNICO_1954D'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_AE526 = layout.box()
        box_AE526.alert = False
        box_AE526.enabled = True
        box_AE526.active = True
        box_AE526.use_property_split = False
        box_AE526.use_property_decorate = False
        box_AE526.alignment = 'Expand'.upper()
        box_AE526.scale_x = 1.0
        box_AE526.scale_y = 1.0
        if not True: box_AE526.operator_context = "EXEC_DEFAULT"
        col_DCAA3 = box_AE526.column(heading='', align=False)
        col_DCAA3.alert = False
        col_DCAA3.enabled = True
        col_DCAA3.active = True
        col_DCAA3.use_property_split = False
        col_DCAA3.use_property_decorate = False
        col_DCAA3.scale_x = 1.0
        col_DCAA3.scale_y = 1.0
        col_DCAA3.alignment = 'Expand'.upper()
        col_DCAA3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_DCAA3.prop(bpy.context.scene, 'sna_pr_cadastro_id', text='ID do Cadastro Arquitetônico', icon_value=0, emboss=True)
        op = col_DCAA3.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EXCLUIR__DIAGNSTICO_DANO_22B33(bpy.types.Panel):
    bl_label = 'Excluir - Diagnóstico Dano'
    bl_idname = 'SNA_PT_EXCLUIR__DIAGNSTICO_DANO_22B33'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_2B716 = layout.box()
        box_2B716.alert = False
        box_2B716.enabled = True
        box_2B716.active = True
        box_2B716.use_property_split = False
        box_2B716.use_property_decorate = False
        box_2B716.alignment = 'Expand'.upper()
        box_2B716.scale_x = 1.0
        box_2B716.scale_y = 1.0
        if not True: box_2B716.operator_context = "EXEC_DEFAULT"
        col_201D2 = box_2B716.column(heading='', align=False)
        col_201D2.alert = False
        col_201D2.enabled = True
        col_201D2.active = True
        col_201D2.use_property_split = False
        col_201D2.use_property_decorate = False
        col_201D2.scale_x = 1.0
        col_201D2.scale_y = 1.0
        col_201D2.alignment = 'Expand'.upper()
        col_201D2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_201D2.prop(bpy.context.scene, 'sna_pr_diagnostico_id', text='ID do Diagnóstico', icon_value=0, emboss=True)
        op = col_201D2.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EXCLUIR_GEOMETRIA_DANO_320F3(bpy.types.Panel):
    bl_label = 'Excluir- Geometria Dano'
    bl_idname = 'SNA_PT_EXCLUIR_GEOMETRIA_DANO_320F3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_68438 = layout.box()
        box_68438.alert = False
        box_68438.enabled = True
        box_68438.active = True
        box_68438.use_property_split = False
        box_68438.use_property_decorate = False
        box_68438.alignment = 'Expand'.upper()
        box_68438.scale_x = 1.0
        box_68438.scale_y = 1.0
        if not True: box_68438.operator_context = "EXEC_DEFAULT"
        col_FAB7D = box_68438.column(heading='', align=False)
        col_FAB7D.alert = False
        col_FAB7D.enabled = True
        col_FAB7D.active = True
        col_FAB7D.use_property_split = False
        col_FAB7D.use_property_decorate = False
        col_FAB7D.scale_x = 1.0
        col_FAB7D.scale_y = 1.0
        col_FAB7D.alignment = 'Expand'.upper()
        col_FAB7D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_FAB7D.prop(bpy.context.scene, 'sna_pr_geometria_id', text='ID da Geometria', icon_value=0, emboss=True)
        op = col_FAB7D.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EXCLUIR__ARQUIVOS_AA0E3(bpy.types.Panel):
    bl_label = 'Excluir - Arquivo(s)'
    bl_idname = 'SNA_PT_EXCLUIR__ARQUIVOS_AA0E3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_63D1A = layout.box()
        box_63D1A.alert = False
        box_63D1A.enabled = True
        box_63D1A.active = True
        box_63D1A.use_property_split = False
        box_63D1A.use_property_decorate = False
        box_63D1A.alignment = 'Expand'.upper()
        box_63D1A.scale_x = 1.0
        box_63D1A.scale_y = 1.0
        if not True: box_63D1A.operator_context = "EXEC_DEFAULT"
        col_82A2C = box_63D1A.column(heading='', align=False)
        col_82A2C.alert = False
        col_82A2C.enabled = True
        col_82A2C.active = True
        col_82A2C.use_property_split = False
        col_82A2C.use_property_decorate = False
        col_82A2C.scale_x = 1.0
        col_82A2C.scale_y = 1.0
        col_82A2C.alignment = 'Expand'.upper()
        col_82A2C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_82A2C.prop(bpy.context.scene, 'sna_pr_bin_file_id_download', text='File ID', icon_value=0, emboss=True)
        op = col_82A2C.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EDITAR__EDIFICAO_FB3C5(bpy.types.Panel):
    bl_label = 'Editar - Edificação'
    bl_idname = 'SNA_PT_EDITAR__EDIFICAO_FB3C5'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_21C05 = layout.box()
        box_21C05.alert = False
        box_21C05.enabled = True
        box_21C05.active = True
        box_21C05.use_property_split = False
        box_21C05.use_property_decorate = False
        box_21C05.alignment = 'Expand'.upper()
        box_21C05.scale_x = 1.0
        box_21C05.scale_y = 1.0
        if not True: box_21C05.operator_context = "EXEC_DEFAULT"
        col_BAFF2 = box_21C05.column(heading='', align=False)
        col_BAFF2.alert = False
        col_BAFF2.enabled = True
        col_BAFF2.active = True
        col_BAFF2.use_property_split = False
        col_BAFF2.use_property_decorate = False
        col_BAFF2.scale_x = 1.0
        col_BAFF2.scale_y = 1.0
        col_BAFF2.alignment = 'Expand'.upper()
        col_BAFF2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_BAFF2.prop(bpy.context.scene, 'sna_pr_edf_id', text='ID Edificação', icon_value=0, emboss=True, toggle=False)
        col_BAFF2.prop(bpy.context.scene, 'sna_pr_edf_nome', text='Nome', icon_value=0, emboss=True)
        col_BAFF2.prop(bpy.context.scene, 'sna_pr_edf_data_construcao', text='Data de Construção', icon_value=0, emboss=True)
        col_BAFF2.prop(bpy.context.scene, 'sna_pr_edf_nome', text='Valor Patrimonial', icon_value=0, emboss=True)
        col_BAFF2.prop(bpy.context.scene, 'sna_pr_edf_descricao_historica', text='Descriçao Histórica', icon_value=0, emboss=True)
        op = col_BAFF2.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EDITAR__USURIO_680BD(bpy.types.Panel):
    bl_label = 'Editar - Usuário'
    bl_idname = 'SNA_PT_EDITAR__USURIO_680BD'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_9756D = layout.box()
        box_9756D.alert = False
        box_9756D.enabled = True
        box_9756D.active = True
        box_9756D.use_property_split = False
        box_9756D.use_property_decorate = False
        box_9756D.alignment = 'Expand'.upper()
        box_9756D.scale_x = 1.0
        box_9756D.scale_y = 1.0
        if not True: box_9756D.operator_context = "EXEC_DEFAULT"
        col_8B1C8 = box_9756D.column(heading='', align=False)
        col_8B1C8.alert = False
        col_8B1C8.enabled = True
        col_8B1C8.active = True
        col_8B1C8.use_property_split = False
        col_8B1C8.use_property_decorate = False
        col_8B1C8.scale_x = 1.0
        col_8B1C8.scale_y = 1.0
        col_8B1C8.alignment = 'Expand'.upper()
        col_8B1C8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_8B1C8.prop(bpy.context.scene, 'sna_pr_userid', text='ID do Usuário', icon_value=0, emboss=False, expand=False)
        col_8B1C8.prop(bpy.context.scene, 'sna_pr_user_nome', text='Nome', icon_value=0, emboss=True)
        col_8B1C8.prop(bpy.context.scene, 'sna_pr_username', text='Username', icon_value=0, emboss=True)
        col_8B1C8.prop(bpy.context.scene, 'sna_pr_user_email', text='Email', icon_value=0, emboss=True)
        col_8B1C8.prop(bpy.context.scene, 'sna_pr_password', text='Password', icon_value=0, emboss=True)
        col_8B1C8.prop(bpy.context.scene, 'sna_pr_user_formacao', text='Formação Acadêmica', icon_value=0, emboss=True)
        col_8B1C8.prop(bpy.context.scene, 'sna_pr_user_data_nascimento', text='Data de Nascimento', icon_value=0, emboss=True)
        op = col_8B1C8.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EDITAR__CADASTRO_ARQUITETNICO_709C1(bpy.types.Panel):
    bl_label = 'Editar - Cadastro Arquitetônico'
    bl_idname = 'SNA_PT_EDITAR__CADASTRO_ARQUITETNICO_709C1'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_C9582 = layout.box()
        box_C9582.alert = False
        box_C9582.enabled = True
        box_C9582.active = True
        box_C9582.use_property_split = False
        box_C9582.use_property_decorate = False
        box_C9582.alignment = 'Expand'.upper()
        box_C9582.scale_x = 1.0
        box_C9582.scale_y = 1.0
        if not True: box_C9582.operator_context = "EXEC_DEFAULT"
        col_4C3D3 = box_C9582.column(heading='', align=False)
        col_4C3D3.alert = False
        col_4C3D3.enabled = True
        col_4C3D3.active = True
        col_4C3D3.use_property_split = False
        col_4C3D3.use_property_decorate = False
        col_4C3D3.scale_x = 1.0
        col_4C3D3.scale_y = 1.0
        col_4C3D3.alignment = 'Expand'.upper()
        col_4C3D3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_4C3D3.prop(bpy.context.scene, 'sna_pr_cadastro_id', text='ID do Cadastro Arquitetônico', icon_value=0, emboss=True)
        col_4C3D3.prop(bpy.context.scene, 'sna_pr_cadastro_id_edificacao', text='ID da Edificação', icon_value=0, emboss=True)
        col_4C3D3.prop(bpy.context.scene, 'sna_pr_cadastro_id_user', text='ID do Usuário', icon_value=0, emboss=True)
        col_4C3D3.prop(bpy.context.scene, 'sna_pr_cadastro_data', text='Data de Cadastro', icon_value=0, emboss=True)
        col_4C3D3.prop(bpy.context.scene, 'sna_pr_cadastro_responsavel_tecnico', text='Responsável Técnico', icon_value=0, emboss=True)
        col_4C3D3.prop(bpy.context.scene, 'sna_pr_cadastro_id_arquivo', text='ID do Arquivo', icon_value=0, emboss=True)
        op = col_4C3D3.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_PT_EDITAR__DIAGNSTICO_DANO_C196A(bpy.types.Panel):
    bl_label = 'Editar - Diagnóstico Dano'
    bl_idname = 'SNA_PT_EDITAR__DIAGNSTICO_DANO_C196A'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_15FAF = layout.box()
        box_15FAF.alert = False
        box_15FAF.enabled = True
        box_15FAF.active = True
        box_15FAF.use_property_split = False
        box_15FAF.use_property_decorate = False
        box_15FAF.alignment = 'Expand'.upper()
        box_15FAF.scale_x = 1.0
        box_15FAF.scale_y = 1.0
        if not True: box_15FAF.operator_context = "EXEC_DEFAULT"
        col_69AB0 = box_15FAF.column(heading='', align=False)
        col_69AB0.alert = False
        col_69AB0.enabled = True
        col_69AB0.active = True
        col_69AB0.use_property_split = False
        col_69AB0.use_property_decorate = False
        col_69AB0.scale_x = 1.0
        col_69AB0.scale_y = 1.0
        col_69AB0.alignment = 'Expand'.upper()
        col_69AB0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_69AB0.prop(bpy.context.scene, 'sna_pr_diagnostico_id', text='ID do Diagnóstico', icon_value=0, emboss=True)
        col_69AB0.prop(bpy.context.scene, 'sna_pr_diagnostico_nome', text='Nome do Dano:', icon_value=0, emboss=True)
        col_69AB0.prop(bpy.context.scene, 'sna_pr_diagnostico_agente_dano', text='Agente(s)', icon_value=0, emboss=True, slider=False, toggle=False)
        col_69AB0.prop(bpy.context.scene, 'sna_pr_diagnostico_descricao_causa', text='Possíveis Causas', icon_value=0, emboss=True)
        col_69AB0.prop(bpy.context.scene, 'sna_pr_diagnostico_relacao_elem_const', text='Elemento de construçao associado(s)', icon_value=0, emboss=True)
        col_69AB0.prop(self, 'self', text='ID do Cadastro relacionado', icon_value=0, emboss=True)
        col_69AB0.prop(bpy.context.scene, 'sna_pr_diagnostico_id_tipo_dano', text='ID do Tipo do Dano', icon_value=0, emboss=True)
        col_69AB0.prop(bpy.context.scene, 'sna_pr_diagnostico_geometria', text='ID Geometria do Elemento', icon_value=0, emboss=True)
        col_69AB0.prop(bpy.context.scene, 'sna_pr_diagnostico_id_arquivo', text='ID dos Arquivo Associados.', icon_value=0, emboss=True)
        op = col_69AB0.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=False, depress=False)


class SNA_PT_EDITAR_GEOMETRIA_DANO_841DA(bpy.types.Panel):
    bl_label = 'Editar- Geometria Dano'
    bl_idname = 'SNA_PT_EDITAR_GEOMETRIA_DANO_841DA'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'ArchPath'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_B0876 = layout.box()
        box_B0876.alert = False
        box_B0876.enabled = True
        box_B0876.active = True
        box_B0876.use_property_split = False
        box_B0876.use_property_decorate = False
        box_B0876.alignment = 'Expand'.upper()
        box_B0876.scale_x = 1.0
        box_B0876.scale_y = 1.0
        if not True: box_B0876.operator_context = "EXEC_DEFAULT"
        col_41E2D = box_B0876.column(heading='', align=False)
        col_41E2D.alert = False
        col_41E2D.enabled = True
        col_41E2D.active = True
        col_41E2D.use_property_split = False
        col_41E2D.use_property_decorate = False
        col_41E2D.scale_x = 1.0
        col_41E2D.scale_y = 1.0
        col_41E2D.alignment = 'Expand'.upper()
        col_41E2D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_41E2D.prop(bpy.context.scene, 'sna_pr_geometria_id', text='ID da Geometria', icon_value=0, emboss=True)
        col_41E2D.prop(bpy.context.scene, 'sna_pr_geometria_global_id_ifc', text='Global ID IFC', icon_value=0, emboss=True)
        col_41E2D.prop(bpy.context.scene, 'sna_pr_geometria_id_arquivo', text='ID do Arquivo correspondente', icon_value=0, emboss=True)
        op = col_41E2D.operator('sn.dummy_button_operator', text='Enviar', icon_value=0, emboss=True, depress=False)


class SNA_AddonPreferences_E32A9(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        if not (False):
            layout = self.layout 
            box_2615F = layout.box()
            box_2615F.alert = False
            box_2615F.enabled = True
            box_2615F.active = True
            box_2615F.use_property_split = False
            box_2615F.use_property_decorate = False
            box_2615F.alignment = 'Expand'.upper()
            box_2615F.scale_x = 1.0
            box_2615F.scale_y = 1.0
            if not True: box_2615F.operator_context = "EXEC_DEFAULT"
            box_2615F.label(text='Login', icon_value=736)
            box_2615F.prop(bpy.context.scene, 'sna_pr_url', text='url', icon_value=0, emboss=True)
            box_2615F.prop(bpy.context.scene, 'sna_pr_username', text='username', icon_value=0, emboss=True)
            box_2615F.prop(bpy.context.scene, 'sna_pr_password', text='password', icon_value=0, emboss=True)
            row_0BA7A = box_2615F.row(heading='', align=False)
            row_0BA7A.alert = False
            row_0BA7A.enabled = True
            row_0BA7A.active = True
            row_0BA7A.use_property_split = False
            row_0BA7A.use_property_decorate = False
            row_0BA7A.scale_x = 1.0
            row_0BA7A.scale_y = 1.0
            row_0BA7A.alignment = 'Expand'.upper()
            row_0BA7A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = row_0BA7A.operator('sna.archpath_op_connect_19b86', text='connect', icon_value=0, emboss=True, depress=False)
            op = row_0BA7A.operator('sna.archpath_op_disconnect_783ee', text='disconnect', icon_value=0, emboss=True, depress=False)
            row_57CA9 = box_2615F.row(heading='', align=False)
            row_57CA9.alert = False
            row_57CA9.enabled = True
            row_57CA9.active = True
            row_57CA9.use_property_split = False
            row_57CA9.use_property_decorate = False
            row_57CA9.scale_x = 1.0
            row_57CA9.scale_y = 1.0
            row_57CA9.alignment = 'Left'.upper()
            row_57CA9.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_57CA9.label(text='status:', icon_value=0)
            row_57CA9.label(text=bpy.context.scene.sna_pr_connection_status, icon_value=0)
            box_8FAC2 = layout.box()
            box_8FAC2.alert = False
            box_8FAC2.enabled = True
            box_8FAC2.active = True
            box_8FAC2.use_property_split = False
            box_8FAC2.use_property_decorate = True
            box_8FAC2.alignment = 'Expand'.upper()
            box_8FAC2.scale_x = 1.0
            box_8FAC2.scale_y = 1.0
            if not True: box_8FAC2.operator_context = "EXEC_DEFAULT"
            box_8FAC2.prop(bpy.context.scene, 'sna_pr_temp_folder_path', text='set temporary folder path', icon_value=0, emboss=True)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_pr_username = bpy.props.StringProperty(name='pr_username', description='', options={'TEXTEDIT_UPDATE'}, default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_password = bpy.props.StringProperty(name='pr_password', description='', default='', subtype='PASSWORD', maxlen=0)
    bpy.types.Scene.sna_pr_url = bpy.props.StringProperty(name='pr_url', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_temp_folder_path = bpy.props.StringProperty(name='pr_temp_folder_path', description='', default='', subtype='DIR_PATH', maxlen=0)
    bpy.types.Scene.sna_pr_connection_status = bpy.props.StringProperty(name='pr_connection_status', description='', default='not conneted', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_edf_nome = bpy.props.StringProperty(name='pr_edf_nome', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_edf_descricao_historica = bpy.props.StringProperty(name='pr_edf_descricao_historica', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_edf_data_construcao = bpy.props.StringProperty(name='pr_edf_data_construcao', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_edf_valor_patrimonial = bpy.props.StringProperty(name='pr_edf_valor_patrimonial', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_user_nome = bpy.props.StringProperty(name='pr_user_nome', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_user_email = bpy.props.StringProperty(name='pr_user_email', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_user_formacao = bpy.props.StringProperty(name='pr_user_formacao', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_user_data_nascimento = bpy.props.IntProperty(name='pr_user_data_nascimento', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_cadastro_id_user = bpy.props.IntProperty(name='pr_cadastro_id_user', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_cadastro_data = bpy.props.StringProperty(name='pr_cadastro_data', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_cadastro_responsavel_tecnico = bpy.props.StringProperty(name='pr_cadastro_responsavel_tecnico', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_cadastro_id_arquivo = bpy.props.IntProperty(name='pr_cadastro_id_arquivo', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_cadastro_id_edificacao = bpy.props.IntProperty(name='pr_cadastro_id_edificacao', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_diagnostico_nome = bpy.props.StringProperty(name='pr_diagnostico_nome', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_diagnostico_agente_dano = bpy.props.StringProperty(name='pr_diagnostico_agente_dano', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_diagnostico_descricao_causa = bpy.props.StringProperty(name='pr_diagnostico_descricao_causa', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_diagnostico_relacao_elem_const = bpy.props.StringProperty(name='pr_diagnostico_relacao_elem_const', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_diagnostico_id_cadastro = bpy.props.IntProperty(name='pr_diagnostico_id_cadastro', description='', default=0, subtype='NONE', update=sna_update_sna_pr_diagnostico_id_cadastro_9275B)
    bpy.types.Scene.sna_pr_diagnostico_id_tipo_dano = bpy.props.IntProperty(name='pr_diagnostico_id_tipo_dano', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_diagnostico_geometria = bpy.props.StringProperty(name='pr_diagnostico_geometria', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_diagnostico_id_arquivo = bpy.props.IntProperty(name='pr_diagnostico_id_arquivo', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_geometria_global_id_ifc = bpy.props.StringProperty(name='pr_geometria_global_id_ifc', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_geometria_id_arquivo = bpy.props.StringProperty(name='pr_geometria_id_arquivo', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_bin_file_filename = bpy.props.StringProperty(name='pr_bin_file_filename', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_bin_file_content = bpy.props.StringProperty(name='pr_bin_file_content', description='', default='', subtype='BYTE_STRING', maxlen=0)
    bpy.types.Scene.sna_pr_bin_file_id_download = bpy.props.StringProperty(name='pr_bin_file_id_download', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_pr_userid = bpy.props.IntProperty(name='pr_userid', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_edf_id = bpy.props.IntProperty(name='pr_edf_id', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_cadastro_id = bpy.props.IntProperty(name='pr_cadastro_id', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_diagnostico_id = bpy.props.IntProperty(name='pr_diagnostico_id', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_pr_geometria_id = bpy.props.IntProperty(name='pr_geometria_id', description='', default=0, subtype='NONE')
    bpy.utils.register_class(SNA_OT_Archpath_Op_Connect_19B86)
    bpy.utils.register_class(SNA_OT_Archpath_Op_Disconnect_783Ee)
    bpy.utils.register_class(SNA_OT_Archpath_Op_Edificacao_Post_940Dc)
    bpy.utils.register_class(SNA_PT_CADASTRAR__EDIFICAO_B585A)
    bpy.utils.register_class(SNA_PT_CADASTRAR__USURIO_2CEF3)
    bpy.utils.register_class(SNA_PT_CADASTRAR__CADASTRO_ARQUITETNICO_9722D)
    bpy.utils.register_class(SNA_PT_CADASTRAR__DIAGNSTICO_DANO_F7238)
    bpy.utils.register_class(SNA_PT_CADASTRAR__GEOMETRIA_DANO_5C854)
    bpy.utils.register_class(SNA_PT_INSERIR__ARQUIVO_8D1E0)
    bpy.utils.register_class(SNA_PT_PESQUISAR__EDIFICAO_09595)
    bpy.utils.register_class(SNA_PT_PESQUISAR_USURIO_E4B88)
    bpy.utils.register_class(SNA_PT_PESQUISAR_CADASTRO_ARQUITETNICO_D2668)
    bpy.utils.register_class(SNA_PT_PESQUISAR__DIAGNSTICO_DANO_32B58)
    bpy.utils.register_class(SNA_PT_PESQUISAR__GEOMETRIA_DANO_079E6)
    bpy.utils.register_class(SNA_PT_DOWNLOAD__ARQUIVOS_4E3A0)
    bpy.utils.register_class(SNA_PT_EXCLUIR__EDIFICAO_2E503)
    bpy.utils.register_class(SNA_PT_EXCLUIR__USURIO_39D2E)
    bpy.utils.register_class(SNA_PT_EXCLUIR__CADASTRO_ARQUITETNICO_1954D)
    bpy.utils.register_class(SNA_PT_EXCLUIR__DIAGNSTICO_DANO_22B33)
    bpy.utils.register_class(SNA_PT_EXCLUIR_GEOMETRIA_DANO_320F3)
    bpy.utils.register_class(SNA_PT_EXCLUIR__ARQUIVOS_AA0E3)
    bpy.utils.register_class(SNA_PT_EDITAR__EDIFICAO_FB3C5)
    bpy.utils.register_class(SNA_PT_EDITAR__USURIO_680BD)
    bpy.utils.register_class(SNA_PT_EDITAR__CADASTRO_ARQUITETNICO_709C1)
    bpy.utils.register_class(SNA_PT_EDITAR__DIAGNSTICO_DANO_C196A)
    bpy.utils.register_class(SNA_PT_EDITAR_GEOMETRIA_DANO_841DA)
    bpy.utils.register_class(SNA_AddonPreferences_E32A9)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_pr_geometria_id
    del bpy.types.Scene.sna_pr_diagnostico_id
    del bpy.types.Scene.sna_pr_cadastro_id
    del bpy.types.Scene.sna_pr_edf_id
    del bpy.types.Scene.sna_pr_userid
    del bpy.types.Scene.sna_pr_bin_file_id_download
    del bpy.types.Scene.sna_pr_bin_file_content
    del bpy.types.Scene.sna_pr_bin_file_filename
    del bpy.types.Scene.sna_pr_geometria_id_arquivo
    del bpy.types.Scene.sna_pr_geometria_global_id_ifc
    del bpy.types.Scene.sna_pr_diagnostico_id_arquivo
    del bpy.types.Scene.sna_pr_diagnostico_geometria
    del bpy.types.Scene.sna_pr_diagnostico_id_tipo_dano
    del bpy.types.Scene.sna_pr_diagnostico_id_cadastro
    del bpy.types.Scene.sna_pr_diagnostico_relacao_elem_const
    del bpy.types.Scene.sna_pr_diagnostico_descricao_causa
    del bpy.types.Scene.sna_pr_diagnostico_agente_dano
    del bpy.types.Scene.sna_pr_diagnostico_nome
    del bpy.types.Scene.sna_pr_cadastro_id_edificacao
    del bpy.types.Scene.sna_pr_cadastro_id_arquivo
    del bpy.types.Scene.sna_pr_cadastro_responsavel_tecnico
    del bpy.types.Scene.sna_pr_cadastro_data
    del bpy.types.Scene.sna_pr_cadastro_id_user
    del bpy.types.Scene.sna_pr_user_data_nascimento
    del bpy.types.Scene.sna_pr_user_formacao
    del bpy.types.Scene.sna_pr_user_email
    del bpy.types.Scene.sna_pr_user_nome
    del bpy.types.Scene.sna_pr_edf_valor_patrimonial
    del bpy.types.Scene.sna_pr_edf_data_construcao
    del bpy.types.Scene.sna_pr_edf_descricao_historica
    del bpy.types.Scene.sna_pr_edf_nome
    del bpy.types.Scene.sna_pr_connection_status
    del bpy.types.Scene.sna_pr_temp_folder_path
    del bpy.types.Scene.sna_pr_url
    del bpy.types.Scene.sna_pr_password
    del bpy.types.Scene.sna_pr_username
    bpy.utils.unregister_class(SNA_OT_Archpath_Op_Connect_19B86)
    bpy.utils.unregister_class(SNA_OT_Archpath_Op_Disconnect_783Ee)
    bpy.utils.unregister_class(SNA_OT_Archpath_Op_Edificacao_Post_940Dc)
    bpy.utils.unregister_class(SNA_PT_CADASTRAR__EDIFICAO_B585A)
    bpy.utils.unregister_class(SNA_PT_CADASTRAR__USURIO_2CEF3)
    bpy.utils.unregister_class(SNA_PT_CADASTRAR__CADASTRO_ARQUITETNICO_9722D)
    bpy.utils.unregister_class(SNA_PT_CADASTRAR__DIAGNSTICO_DANO_F7238)
    bpy.utils.unregister_class(SNA_PT_CADASTRAR__GEOMETRIA_DANO_5C854)
    bpy.utils.unregister_class(SNA_PT_INSERIR__ARQUIVO_8D1E0)
    bpy.utils.unregister_class(SNA_PT_PESQUISAR__EDIFICAO_09595)
    bpy.utils.unregister_class(SNA_PT_PESQUISAR_USURIO_E4B88)
    bpy.utils.unregister_class(SNA_PT_PESQUISAR_CADASTRO_ARQUITETNICO_D2668)
    bpy.utils.unregister_class(SNA_PT_PESQUISAR__DIAGNSTICO_DANO_32B58)
    bpy.utils.unregister_class(SNA_PT_PESQUISAR__GEOMETRIA_DANO_079E6)
    bpy.utils.unregister_class(SNA_PT_DOWNLOAD__ARQUIVOS_4E3A0)
    bpy.utils.unregister_class(SNA_PT_EXCLUIR__EDIFICAO_2E503)
    bpy.utils.unregister_class(SNA_PT_EXCLUIR__USURIO_39D2E)
    bpy.utils.unregister_class(SNA_PT_EXCLUIR__CADASTRO_ARQUITETNICO_1954D)
    bpy.utils.unregister_class(SNA_PT_EXCLUIR__DIAGNSTICO_DANO_22B33)
    bpy.utils.unregister_class(SNA_PT_EXCLUIR_GEOMETRIA_DANO_320F3)
    bpy.utils.unregister_class(SNA_PT_EXCLUIR__ARQUIVOS_AA0E3)
    bpy.utils.unregister_class(SNA_PT_EDITAR__EDIFICAO_FB3C5)
    bpy.utils.unregister_class(SNA_PT_EDITAR__USURIO_680BD)
    bpy.utils.unregister_class(SNA_PT_EDITAR__CADASTRO_ARQUITETNICO_709C1)
    bpy.utils.unregister_class(SNA_PT_EDITAR__DIAGNSTICO_DANO_C196A)
    bpy.utils.unregister_class(SNA_PT_EDITAR_GEOMETRIA_DANO_841DA)
    bpy.utils.unregister_class(SNA_AddonPreferences_E32A9)
