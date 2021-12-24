$(function(){
   var cnt = 0;
   var q_arr = q;
   var ans1_arr = ans1;
   var ans2_arr = ans2;

   var label = $('#label');
   var bt1 = $('#bt1');
   var bt2 = $('#bt2');

   var total_answer = [];

   label.text(q_arr[0]);
   bt1.text(ans1_arr[0]);
   bt2.text(ans2_arr[0]);

   $('.select').click(function(){
      console.log($(this).text());
      total_answer.push($(this).text());
      cnt++;
      label.text(q_arr[cnt]);
      bt1.text(ans1_arr[cnt]);
      bt2.text(ans2_arr[cnt]);

      if(cnt==15){
         location.href='/ready?answer='+total_answer;
         console.log(total_answer);
      }
   })
   $('#home').click(function(){
       location.href='/'
   });
   $('#refresh').click(function(){
       location.href='/qna'
   });
});
