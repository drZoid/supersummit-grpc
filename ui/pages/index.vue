<template>
  <div class="container">
    <button type="button" @click="fetchMovie()" title="Click here for best western movie ever!">GetMovie</button>
    <div class="detail"> Movie Name: {{movieName}} </div>
    <div class="detail"> Movie Overview: {{movieOverview}} </div>
    <div class="detail"> Top Cast: {{topCast}} </div>
    <div class="detail"> Year: {{year}} </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "nuxt-property-decorator";
import * as MoviesPb from "@superset/grpc-protobuf-client-js/western_movies_pb";

@Component({})
export default class Index extends Vue {

  protected movieName= ""
  protected movieOverview = ""
  protected topCast = ""
  protected year = ""

  fetchMovie() {
    const request = new MoviesPb.NameRequest().setName("foobarbazqux");
    const response = this.$movieClient.getByName(request, null)
    response.then((value) => {
      this.movieName = value.getName()
      this.movieOverview = value.getOverview();
      this.topCast = value.getTopcast();
      this.year = value.getYear();
    })
  }
}
</script>
<style scoped>
.detail {
    font-size: large;
    margin-left: 40%;
}
.container {
   margin-top: 10%;
}
</style>
