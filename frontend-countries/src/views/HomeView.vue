<template>
  <div class="bg-white py-6 sm:py-8 lg:py-12">
    <div class="max-w-screen-2xl px-4 md:px-8 mx-auto">
      <!-- text - start -->
      <div class="mb-10 md:mb-16">
        <h2
          class="text-gray-800 text-2xl lg:text-3xl font-bold text-center mb-4 md:mb-6"
        >
          Product Form
        </h2>

        <p class="max-w-screen-md text-gray-500 md:text-lg text-center mx-auto">
          Test product Form with Countries dropdown.
        </p>
      </div>
      <!-- text - end -->

      <!-- form - start -->
      <form
        class="max-w-screen-md grid sm:grid-cols-2 gap-4 mx-auto"
        @submit.prevent="submitProduct"
      >
        <div>
          <label
            for="name"
            class="inline-block text-gray-800 text-sm sm:text-base mb-2"
            >Name*</label
          >
          <input
            v-model="product.name"
            name="name"
            type="text"
            class="w-full bg-gray-50 text-gray-800 border focus:ring ring-indigo-300 rounded outline-none transition duration-100 px-3 py-2"
          />
        </div>

        <div>
          <label
            for="price"
            class="inline-block text-gray-800 text-sm sm:text-base mb-2"
            >Price*</label
          >
          <input
            v-model="product.price"
            name="price"
            type="number"
            class="w-full bg-gray-50 text-gray-800 border focus:ring ring-indigo-300 rounded outline-none transition duration-100 px-3 py-2"
          />
        </div>

        <div class="sm:col-span-2">
          <label
            for="country"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400"
            >Country</label
          >
          <select
            v-model="product.country"
            name="country"
            class="w-full bg-gray-50 text-gray-800 border focus:ring ring-indigo-300 rounded outline-none transition duration-100 px-3 py-2"
          >
            <option value="none">Choose a country</option>
            <option v-for="(name, key) in countries" :key="key" :value="key">
              {{ name }}
            </option>
          </select>
        </div>

        <div class="sm:col-span-2">
          <label
            for="description"
            class="inline-block text-gray-800 text-sm sm:text-base mb-2"
            >Description*</label
          >
          <textarea
            v-model="product.discription"
            rows="3"
            name="description"
            class="w-full h-50 bg-gray-50 text-gray-800 border focus:ring ring-indigo-300 rounded outline-none transition duration-100 px-3 py-2"
          ></textarea>
        </div>

        <div class="sm:col-span-2 flex justify-between items-center">
          <button
            type="submit"
            class="inline-block bg-indigo-500 hover:bg-indigo-600 active:bg-indigo-700 focus-visible:ring ring-indigo-300 text-white text-sm md:text-base font-semibold text-center rounded-lg outline-none transition duration-100 px-8 py-3"
          >
            save
          </button>

          <span class="text-gray-500 text-sm">*Required</span>
        </div>
      </form>
      <!-- form - end -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HomeView",
  data() {
    return {
      product: {
        name: "",
        price: "",
        country: "none",
        discription: "",
      },
      countries: "",
    };
  },
  mounted() {
    this.getCountries();
  },
  methods: {
    getCountries() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/countries_list/",
      }).then((response) => {
        this.countries = response.data;
      });
    },
    submitProduct() {
      let productData = new FormData();
      productData.append("product_Name", this.product.name);
      productData.append("price", this.product.price);
      productData.append("country", this.product.country);
      productData.append("product_discriptions", this.product.discription);

      // Display the key/value pairs
      // for (var pair of productData.entries()) {
      //   console.log(pair[0] + ", " + pair[1]);
      // }

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/v1/products/",
        data: productData,
      }).then(() => {
        this.product = {
          name: "",
          price: "",
          country: "none",
          discription: "",
        };
      });
    },
  },
};
</script>
