<script lang="ts">
	import logo from '$lib/images/logo.png';
</script>

<header class="bg-custom_black-500 shadow-md h-20">
	<div class="w-20">
		<a href="/" class="flex items-center gap-4 absolute left-20 top-3">
			<img src="{logo}" alt="Logo"
				class="logo max-w-14"
			>
			<div class="text-3xl text-white">Pokerzyści</div>
		</a>
	</div>

</header>

<style>
	.logo {
		border-radius: 99999px;
		box-shadow: -4px -2px 7px  oklch(0.865 0.127 207.078),
					4px 2px 7px  oklch(0.496 0.265 301.924);


	}
</style>