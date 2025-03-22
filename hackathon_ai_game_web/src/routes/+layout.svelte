<script lang="ts">
	import Header from "./Header.svelte";
	import "../app.css";

	let { children } = $props();
</script>

<svelte:head>
	<title>Control Panel</title>
</svelte:head>

<div class="bg-custom_white-500 h-[100vh]">

	<Header />

	<div>
		{@render children()}
	</div>

</div>