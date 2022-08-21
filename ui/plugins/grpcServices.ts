import { Plugin } from "@nuxt/types";

import { WesternMoviesClient } from "@superset/grpc-protobuf-client-js/Western_moviesServiceClientPb";

declare module "vue/types/vue" {
  interface Vue {
    $movieClient: WesternMoviesClient;
  }
}

const grpcServicePlugin: Plugin = (context, inject) => {
  const $movieClient = new WesternMoviesClient(context.env.baseUrl, null, {
    withCredentials: true
  })
  inject("movieClient", $movieClient)
}

export default grpcServicePlugin
