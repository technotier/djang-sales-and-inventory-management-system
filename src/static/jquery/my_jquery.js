$(document).ready(function(){

    // This is for hide last five panel
    $("#div_id_line_six_product, #div_id_line_six_qty, #div_id_line_six_price,  #div_id_line_six_total_price, #div_id_line_seven_product, #div_id_line_seven_qty, #div_id_line_seven_price,  #div_id_line_seven_total_price, #div_id_line_eight_product, #div_id_line_eight_qty, #div_id_line_eight_price,  #div_id_line_eight_total_price, #div_id_line_nine_product, #div_id_line_nine_qty, #div_id_line_nine_price,  #div_id_line_nine_total_price, #div_id_line_ten_product, #div_id_line_ten_qty, #div_id_line_ten_price,  #div_id_line_ten_total_price").hide()

    // This id for show last five panel after click
    $('button#more-line').click(function(){
        $("#div_id_line_six_product, #div_id_line_six_qty, #div_id_line_six_price,  #div_id_line_six_total_price").slideToggle(600)
        $("#div_id_line_seven_product, #div_id_line_seven_qty, #div_id_line_seven_price,  #div_id_line_seven_total_price").slideToggle(600)
        $("#div_id_line_eight_product, #div_id_line_eight_qty, #div_id_line_eight_price,  #div_id_line_eight_total_price").slideToggle(600)
        $("#div_id_line_nine_product, #div_id_line_nine_qty, #div_id_line_nine_price,  #div_id_line_nine_total_price").slideToggle(600)
        $("#div_id_line_ten_product, #div_id_line_ten_qty, #div_id_line_ten_price,  #div_id_line_ten_total_price").slideToggle(600)
    });

// Auto calculation
$('#id_line_one_qty, #id_line_one_price, #id_line_two_qty, #id_line_two_price, #id_line_three_qty, #id_line_three_price, #id_line_four_qty, #id_line_four_price, #id_line_five_qty, #id_line_five_price, #id_line_six_qty, #id_line_six_price, #id_line_seven_qty, #id_line_seven_price, #id_line_eight_qty, #id_line_eight_price, #id_line_nine_qty, #id_line_nine_price, #id_line_ten_qty, #id_line_ten_price').keyup(function() {

    var qty_1_text = $('#id_line_one_qty').val();
    var price_1_text = $('#id_line_one_price').val();
    var price_1_total = qty_1_text * price_1_text

    var qty_2_text = $('#id_line_two_qty').val();
    var price_2_text = $('#id_line_two_price').val();
    var price_2_total = qty_2_text * price_2_text

    var qty_3_text = $('#id_line_three_qty').val();
    var price_3_text = $('#id_line_three_price').val();
    var price_3_total = qty_3_text * price_3_text

    var qty_4_text = $('#id_line_four_qty').val();
    var price_4_text = $('#id_line_four_price').val();
    var price_4_total = qty_4_text * price_4_text

    var qty_5_text = $('#id_line_five_qty').val();
    var price_5_text = $('#id_line_five_price').val();
    var price_5_total = qty_5_text * price_5_text

    var qty_6_text = $('#id_line_six_qty').val();
    var price_6_text = $('#id_line_six_price').val();
    var price_6_total = qty_6_text * price_6_text

    var qty_7_text = $('#id_line_seven_qty').val();
    var price_7_text = $('#id_line_seven_price').val();
    var price_7_total = qty_7_text * price_7_text

    var qty_8_text = $('#id_line_eight_qty').val();
    var price_8_text = $('#id_line_eight_price').val();
    var price_8_total = qty_8_text * price_8_text

    var qty_9_text = $('#id_line_nine_qty').val();
    var price_9_text = $('#id_line_nine_price').val();
    var price_9_total = qty_9_text * price_9_text

    var qty_10_text = $('#id_line_ten_qty').val();
    var price_10_text = $('#id_line_ten_price').val();
    var price_10_total = qty_10_text * price_10_text

    var total = price_1_total + price_2_total + price_3_total + price_4_total + price_5_total + price_6_total + price_7_total + price_8_total + price_9_total + price_10_total

    $('#id_line_one_total_price').val((price_1_total));
    $('#id_line_two_total_price').val((price_2_total));
    $('#id_line_three_total_price').val((price_3_total));
    $('#id_line_four_total_price').val((price_4_total));
    $('#id_line_five_total_price').val((price_5_total));
    $('#id_line_six_total_price').val((price_6_total));
    $('#id_line_seven_total_price').val((price_7_total));
    $('#id_line_eight_total_price').val((price_8_total));
    $('#id_line_nine_total_price').val((price_9_total));
    $('#id_line_ten_total_price').val((price_10_total));
    $('#id_total_amount').val(total);
    
});


}); // this is end
