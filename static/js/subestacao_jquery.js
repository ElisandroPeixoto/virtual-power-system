// Seleção da Janela de Operação de cada equipamento

$(document).ready(function(){
    $("input[name$='equipament']").click(function(){
        var valor_equip = $(this).val();

        $("div.box_equipamento").hide();
        $("#equip" + valor_equip).show();
    });
});