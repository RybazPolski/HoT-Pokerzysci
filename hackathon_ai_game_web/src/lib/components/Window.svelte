<script>

    let { children } = $props();

</script>

<div class="w-full">
    <div class="bg-white w-full h-full min-h-96 rounded-lg shadow-lg border border-slate-400 border-[1px] p-4 pl-10">
        <div class="flex justify-between items-center ">

            {@render children()}

        </div>

    </div>

</div>

