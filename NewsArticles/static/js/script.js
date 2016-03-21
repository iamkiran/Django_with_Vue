
  $(document).ready(function() {
	  $('#myCarousel').carousel({
	  interval: 10000

  });
    
    });


window.onload = function () {
  Vue.config.delimiters = ['<%', '%>']
  

   /*var loadArticelOnStartup = new Vue({
      el : '#list-Of-Articles-Displayed',
      data : {



         loadArticles: [
{
        id : "1",
        title:"Chris Chris",
        author_Detail:"Chris",
        date:"2016-03-20T11:27:22Z",
        m_image:"uploadedImg/main/mendeleev_2728229f_QuSB6L3_DTFOfuH.jpg",
        s_Image:"uploadedImg/sub/Pluto_2725059f_1NCg8xJ.jpg",
        body:"Rabada to Mohammad Shahzad, 2 runs, slashes hard at a length ball outside off, and slices it over the covers. The bat twisted in his hands but got it over the infield",
        likecount:"1"
      },
      {
        id : "2",
        title:"kiran",
        author_Detail:"kiran",
        date:"2016-03-20T10:42:14Z",
        m_image:"uploadedImg/main/0a35647a_2728824f_o0hRGER.jpg",
        s_Image:"uploadedImg/sub/Siachan_global_war_2728002f_5Qro0EC.jpg",
        body:"likecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecountlikecount",
        likecount:"4"
      },
     

         ],
          
      } , 
      
      methods:{

      }

   })*/





 var upDownVote = new Vue({
  el: '#onclButton',
  data: {
    countmessage : 0
  },
  methods: {
    upCount: function () { 
     upDownVote.$set('count' , upDownVote.count + 1) ;
      this.$http.get('/article/getVoteCount?count='+upDownVote.count).then(function (response) {
      this.$set('count',upDownVote.count);
      })
    },
    downCount: function(){
     if(upDownVote.count > 0){
        upDownVote.$set('count' , upDownVote.count - 1) ; 
      }
    },
    resetCount:function(){
       upDownVote.$set('count', 0) ;
    },
    
  }
  
})
upDownVote.$set('count', 0);


/*
Vue.component('venue-component', {
    el: '#onclButton',
 
  methods: {
    upCount: function () {
      e.preventDefault()
      upDownVote.$set('count' , upDownVote.count + 1) 
// unlike
      }, function (data) {
        success(function (data, status, request) {
        // handle success
        }).error(function (data, status, request) {
        // handle error
      })
    },
  }
})*/


}













