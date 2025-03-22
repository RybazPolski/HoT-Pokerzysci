<script lang="ts">
	import Header from "./Header.svelte";
	import "../app.css";

	let { children } = $props();
</script>

<svelte:head>
	<title>Control Panel</title>
</svelte:head>

<div class="bg-custom_white-500 h-[100vh] overflow-x-hidden ">

	<div class="sticky top-0 z-50">
		<Header />
	</div>

	<div>
		{@render children()}
	</div>

</div>