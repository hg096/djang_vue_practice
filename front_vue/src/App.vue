<template>
  <!-- <v-app>
    <v-main>
      <HelloWorld/>
    </v-main>
  </v-app> -->
    <div>
      <headerDe></headerDe>
      <!-- v-bind:하위컴포넌트 속성명="상위 컴포넌트 전달할 데이터명"  -->
      <contentDe v-bind:propsdata="userList" v-on:saved="getUserList" v-on:deleted="getUserList" v-on:patched="getUserList" ></contentDe>
      <footerDe></footerDe>
    </div>
</template>

<script>

import HeaderDe from "./components/HeaderDe.vue";
import ContentDe from "./components/ContentDe.vue";
import FooterDe from "./components/FooterDe.vue";
import axios from "axios";

let url = "http://localhost:8000/user/";  // 장고 drf 서버 주소
// import HelloWorld from './components/HelloWorld.vue'

export default {

  data: () => {
    return {
      userList: []
    };
  },

  components: {
    "headerDe" : HeaderDe,
    "contentDe" : ContentDe,
    "footerDe" : FooterDe,
  },

  mounted() { // DOM 객체가 생성된 후 DRF server 에서 데이터를(userList) 가져와 저장
    axios({
      method: "GET",
      url: url
    })
      .then(response => {
        for (var index in response.data) {
          response.data[index].is_hidden = false; // 백에서 받은 데이터에 is_hidden=false 추가
        }
      this.userList = response.data;
      console.log("Success", response);

    })
    .catch(error => {
      console.log("Failed", error.response);
    });
  },

  methods: {  // CRUD 로직
    getUserList: function () {
      axios({
        method: "GET",
        url: url
      })
        .then(response => {
          for (var index in response.data) {
            response.data[index].is_hidden = false; // 백에서 받은 데이터에 is_hidden=false 추가
          }
          this.userList = response.data;
          console.log("Success", response);
        })
        .catch(error => {
          console.log("Failed to get userList", error.response);
        });
    },
    updateUserList: function() {},
    deleteUserList: function() {}
  }

};
</script>
