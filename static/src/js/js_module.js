
//$(document).ready(function(){
//
//      $('button').click(function(){
//      patient_name = $('#patient_name').val()
//      patient_age = $('#patient_age').val()
//      patient_gender = $('#patient_gender').val()
//      notes = $('#patient_notes').val()
//      data={
//      'patient_name':patient_name,
//      'patient_age':patient_age,
//      'patient_gender':patient_gender,
//      'notes':notes
//      }
//      rpc.query({
//      route:'/hospital/patient',
//      params :{'data':data}
//      })
//      })
//
//     })
$(document).ready(function(){
    odoo.define('hospital.patientform', function(require) {
        var rpc = require('web.rpc');
//-----------------------------------------------READ----------------------------------------------
        $('#btn-show-doctors').click(function(){
        $('#btn-show-doctors').hide()
             rpc.query({
            model: 'hospital.doctor',
            method: 'search_read'
                        }).then(function(data){
                            var ul = $('.card-columns')
                            console.log(data)
                             data.forEach((item)=>{
                             console.log(item.doctor_name)
                             ul.append(
                        '<div class="card">'+
                        '<div class="card-body">'+
                      '<h5 class="card-title font-weight-bold">'+item.doctor_name+'</h5>'+
                       '<p class="card-text id="doctor_id>'+'Doctor_id:'+item.doc_id+'</p>'+
                       '<p class="card-text">'+'Age:'+item.doctor_age+'</p>'+
                       '<p class="card-text">'+'Gender:'+item.gender+'</p>'+
                       '<p class="card-text">'+'Speciality:'+item.doctor_speciality+'</p>'+
                       '<p class="card-text">'+'Contact Number:'+item.doctor_phone+'</p>'+
                       '<button type="button" class="btn btn-danger delete-modal" data-toggle="modal" data-target="#deleteModal">'+
                             ' Delete'+
                    '</button>'+
                    '<button type="button" class="btn btn-primary update-modal" data-toggle="modal" data-target="#updateModal">'+
                             'Update'+
                    '</button>'+
                        '</div>'+
                      '</div>'
                             )
                             })
                            console.log(ul)


//                           ----------------------------------------- DELETE-------------------------------------------
                             $('.delete-modal').click(function(){

                                    doc_id = $(this).parent().children().eq(1).text()
                                    doctor = $(this).parent().children().first().text()
                                    doc_id = doc_id.split(":")
                                    $('#delete-btn').click(function(){
                                    $('#deleteModal').modal('hide')
                                    console.log('clicked')
                                        rpc.query({
                                        model:'hospital.doctor',
                                        method:'delete_doctor',
                                        args:[doc_id[1]]
                                        })
                                    })
                                    console.log(doc_id)
                                    console.log(doctor)
                                        })




//----------------------------------_UPDATE----------------------------------------------
                              $('.update-modal').click(function(){
                              console.log('clicked')
                                    doc_id = $(this).parent().children().eq(1).text()
                                    doc_id = doc_id.split(":")
                                    console.log(doc_id)
                                    rpc.query({
                                    model:'hospital.doctor',
                                    method:'get_doctor',
                                    args:[doc_id[1]]
                                    }).then(function(result){
                                        console.log(result)
                                       $('#update_doctor_name').val(result.doctor_name)
                                       $('#update_doctor_age').val(result.doctor_age)
                                       $('#update_doctor_speciality').val(result.doctor_speciality)
                                       $('#update_doctor_phone').val(result.doctor_phone)
                                       $('#update_doctor_gender').val(result.doctor_gender)

                                            $('#update_form-submit').click(function(){

                                              var formObj = {'id':result.id};
                                              var inputs = $('form').serializeArray();
                                                               $.each(inputs, function (i, input) {
                                                            formObj[input.name] = input.value;
                                                        });
                                            delete formObj.csrf_token
                                            console.log(formObj)

                                            rpc.query({
                                            model:'hospital.doctor',
                                            method:'write',
                                            args:[formObj.id,formObj]
                                            })

                                            })


                                    })


                              })
             })
        })

//        document.querySelector('form').addEventListener('submit', (e) => {
//      const data = Object.fromEntries(new FormData(e.target).entries());
//      console.log(data)
//    });

//---------------------------------------CREATE--------------------------------------------------

        $('#form-submit').click(function(){

          var formObj = {};
          var inputs = $('#create-form').serializeArray();
          console.log(inputs)
           $.each(inputs, function (i, input) {
                formObj[input.name] = input.value;
            });
        delete formObj.csrf_token
        console.log(formObj)

        rpc.query({
        model:'hospital.doctor',
        method:'create',
        args:[formObj]
        })

        })




     })
});



//
//$(document).ready(function(){
//    odoo.define('hospital.patientform', function(require) {
//    var rpc = require('web.rpc');
//    rpc.query({
//        model:'hospital.patients',
//        method:'get_patients_list'
//    }).then(function(data){
//        console.log(data)
//        console.log(typeof(data))
//        result=JSON.parse(data)
//        console.log(result)
//        })
//
//    })
//})