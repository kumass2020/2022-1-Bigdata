//������ �ε�
function setDaumMapMarker(map, lat, lng, selectMode ){
    jQuery(".store_locator").addClass("on");jQuery(".store_locator").next(".cont").show();
    jQuery(".store_new").removeClass("on");jQuery(".store_new").next(".cont").hide();

    selectMode != "" ? mode = selectMode : mode = mode ;
    var local = "";
    var local2 = "";
    var keyword = "";
    var sNo_temp = "";

    if (sNo != "" ) {
        mode = 'search';
        sNo_temp = sNo;
        sNo = "";

    } else {
        switch(mode) {
            case 'search' : ( 
                                keyword = jQuery("#keyword").val() != jQuery("#keyword").attr("data-val") && jQuery("#keyword").val() != "" ? jQuery("#keyword").val() : "" , 
                                jQuery("#storeLocal2").html(''),
                                lat = "", lng = ""
                            );	break;
            case 'local' : ( 
                                lat = "", lng = "", 
                                jQuery("#keyword").val('') ,
                                local = ( jQuery("#localTitle").text() != jQuery("#localTitle").attr("data-default") && jQuery("#localTitle").text() != "" ) ? jQuery("#localTitle").text() : "",
                                local2 = ( jQuery("#localTitle2").text() != jQuery("#localTitle2").attr("data-default") && jQuery("#localTitle").text() != "" ) ? jQuery("#localTitle2").text() : ""
                            ); break;
            case 'center' : ( 
                                jQuery("#keyword").val(''),
                                ( lat == "" || lng == ""  ) ? 
                                    ( 
                                        center = map.getCenter(),
                                        lat = center.getLat(), lng = center.getLng() 
                                    ) : "" 
                                ); break;
        }

//			if (jQuery("#petkeyword").val() != "") {
//				keyword = jQuery("#petkeyword").val() != jQuery("#petkeyword").attr("data-val") && jQuery("#petkeyword").val() != "" ? jQuery("#petkeyword").val() : "";
//			}
    }

    //mode == "search" ? ( keyword = jQuery("#keyword").val(), /*jQuery("#keyword").val(''),*/ lat = "", lng = ""  ) : ( keyword = "", jQuery("#keyword").val(''), ( lat == "" || lng == ""  ) ? ( center = map.getCenter(), lat = center.getLat(), lng = center.getLng() ) : "" 	)

    // mode2 - ���� �˻� �϶� �ش� ������ �� ��� ���� �ʱ�ȭ ���ش�
    //mode2 != "" ? ( mode = "search", keyword = "", lat = "", lng = "", jQuery("#keyword").val('') ) : mode = mode ; 
    
    var chk1 = jQuery("#chk1").prop("checked") ? 1 : 0 ; 
    var chk2 = jQuery("#chk2").prop("checked") ? 1 : 0 ; 
    var chk3 = jQuery("#chk3").prop("checked") ? 1 : 0 ; 
    var chk4 = jQuery("#chk4").prop("checked") ? 1 : 0 ; 
    var chk5 = jQuery("#chk5").prop("checked") ? 1 : 0 ; 
    var chk6 = jQuery("#chk6").prop("checked") ? 1 : 0 ; 
    var chk7 = jQuery("#chk7").prop("checked") ? 1 : 0 ; 
    var chk8 = jQuery("#chk8").prop("checked") ? 1 : 0 ; 
    var chk9 = jQuery("#chk9").prop("checked") ? 1 : 0 ; 
    var chk10 = jQuery("#chk10").prop("checked") ? 1 : 0 ; 
    var chk11 = jQuery("#chk11").prop("checked") ? 1 : 0 ; 

    jQuery.ajax({
        type: "GET",
        datatype: "json",
        data : { "lat" : lat, "lng" : lng ,
                "chk1" : chk1 , "chk2" : chk2 , "chk3" : chk3 , "chk4" : chk4 , "chk5" : chk5 , "chk6" : chk6 , "chk7" : chk7 , "chk8" : chk8 , "chk9" : chk9 , "chk10" : chk10 , "chk11" : chk11 , 
                "keyword" : keyword, "StoreLocal" : local, "StoreLocal2" : local2, "storeNo" : sNo_temp },
        url: "store_data2.asp",
        success: function (data) {

            //clusterer.clear();

            //��Ŀ, ���� ������ , ����Ʈ �ʱ�ȭ 
            resetDaumMap();
            positions = eval(data);

            //�˻� �϶� ù��° ������ ���ͷ� ����
            if ( mode != "center" && positions.length > 0 ) {
                map.setCenter( new daum.maps.LatLng(positions[0].StoreLAT, positions[0].StoreLNG) );
            }

            //��Ŀ �����ͷ� �׸���
            positions.length > 0 ? drawDaumMapMarker(positions) : jQuery("#storeListUL").html("<div style='width:100%;text-align:center;margin:50px 0px;'>�˻��� ������ �����ϴ�.</div>");
        }
    })
    //Ű���� �� ��ĭ�̸� �⺻ ������ ä���ش�
    jQuery("#keyword").val() == "" ? jQuery("#keyword").val( jQuery("#keyword").attr("data-val") ) : "" ;
    jQuery("#petkeyword").val() == "" ? jQuery("#petkeyword").val( jQuery("#petkeyword").attr("data-val") ) : "" ;
}