<script lang="ts">
	import Header from "./Header.svelte";
	import "../app.css";
	import {Toaster} from "svelte-sonner";

	let { children } = $props();

</script>

<svelte:head>
	<title>Control Panel</title>
</svelte:head>

<Toaster position="top-right" />

<div class="bg-custom_white-500 h-[100vh] overflow-x-hidden ">

	<div class="sticky top-0 z-50">
		<Header />
	</div>

	<div>
		{@render children()}
	</div>

</div>